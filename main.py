import tkinter as tk
from screeninfo import get_monitors

import json
import threading
import sys


class DarkOverlay(tk.Tk):
    def __init__(self, monitor):
        super().__init__()

        try:
            screen_width = monitor.width
            screen_height = monitor.height
            screen_x = monitor.x
            screen_y = monitor.y

            self.overrideredirect(True)
            self.geometry(f"{screen_width}x{screen_height}+{screen_x}+{screen_y}")
            self.configure(bg="black")

            self.bind("<Double-1>", self.destroy_overlay)

        except Exception as e:
            print(f"Error initializing overlay: {e}", file=sys.stderr)
            self.destroy()

    def destroy_overlay(self, event):
        self.destroy()


def create_overlay(monitor):
    try:
        overlay = DarkOverlay(monitor)
        overlay.mainloop()

    except Exception as e:
        print(f"Error in overlay thread: {e}", file=sys.stderr)


def load_config():
    try:
        with open("./config.json", "r") as file:
            config = json.load(file)

        return config.get("monitors", [])

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config file: {e}", file=sys.stderr)

        return []


if __name__ == "__main__":
    monitors_to_overlay = load_config()
    monitors = get_monitors()

    if not monitors:
        print("No monitors can be detected.", file=sys.stderr)
        sys.exit(1)

    threads = []

    for monitor_idx in monitors_to_overlay:
        if (
            not isinstance(monitor_idx, int)
            or monitor_idx < 0
            or monitor_idx >= len(monitors)
        ):
            print(
                f"Invalid monitor index in config file: {monitor_idx}", file=sys.stderr
            )
            continue

        target_monitor = monitors[monitor_idx]
        thread = threading.Thread(
            target=create_overlay,
            args=(target_monitor,),
        )
        threads.append(thread)
        thread.start()
