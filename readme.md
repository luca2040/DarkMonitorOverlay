# Dark Monitor Overlay

#### _Simple and small program to make monitors completely dark and distraction-free for gaming or general use._

## Download

_See the **release section**._

No installation is needed since this is a portable exe file.

## Description

While gaming i don't like the light coming from other monitors other than the one i am using, so i made this simple program to make them completely black.<br/>
When opened this program creates black fullscreen borderless windows on the monitors specified in the config file.<br/>
Being the overlays borderless windows, you can drag other windows over it.<br/>
**To close an overlay on a monitor, simply double-click on it.**

## Config

The config is specified in a `config.json` file placed in the same path as the program's executable.

Example config to darken monitor `0` and `2`:
```json
{
  "monitors": [
    0,
    2
  ]
}
```