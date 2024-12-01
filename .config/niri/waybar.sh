#!/usr/bin/env bash

killall waybar
pkill waybar
waybar -c ~/.config/niri/waybar/config -s ~/.config/niri/waybar/style.css
