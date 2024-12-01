#!/bin/sh
swayidle -w timeout 300 'swaylock -f -i ~/wallpaper/default.jpg' timeout 600 'niri msg action power-off-monitors' before-sleep 'swaylock -f -i ~/wallpaper/default.jpg'
