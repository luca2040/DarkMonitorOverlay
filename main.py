import tkinter as tk
from screeninfo import get_monitors

import json
import threading


class DarkOverlay(tk.Tk):
    def __init__(self, monitor):
        super().__init__()

        screen_width = monitor.width
        screen_height = monitor.height
        screen_x = monitor.x
        screen_y = monitor.y

        self.overrideredirect(True)

        self.geometry(f"{screen_width}x{screen_height}+{screen_x}+{screen_y}")

        self.configure(bg="black")

        self.bind("<Double-1>", self.destroy_)

    def destroy_(self, event):
        self.destroy()


def create_overlay(monitor):
    overlay = DarkOverlay(monitor)
    overlay.mainloop()


if __name__ == "__main__":
    with open("./config.json", "rb") as file:
        config = json.load(file)

    monitors_to_overlay = config["monitors"]
    monitors = get_monitors()

    threads = []

    for monitor_i in monitors_to_overlay:
        second_monitor = monitors[monitor_i]
        thread = threading.Thread(target=create_overlay, args=(second_monitor,))
        threads.append(thread)
        thread.start()
