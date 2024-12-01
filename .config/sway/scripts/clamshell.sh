#!/usr/bin/bash
# change output
if cat /proc/acpi/button/lid/LID/state | grep -q open; then
    swaymsg output <eDP-1> enable
else
    swaymsg output <eDP-1> disable
fi
