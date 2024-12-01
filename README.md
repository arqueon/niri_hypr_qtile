# Niri, Hyprland and Qtile dotfiles for [Arcolinux](https://www.arcolinux.info/)

## Dependencies

This repository provides _dotfiles_ for a customized desktop environment on [Arcolinux](https://www.arcolinux.info/), featuring the [Niri](https://github.com/YaLTeR/niri) compositor, [Hyprland](https://github.com/hyprwm/Hyprland) and [Qtile](https://github.com/qtile/qtile) window managers.

- **Niri:** A Wayland compositor known for its performance and minimalist design, inspired in PaperWM. 
- **Hyprland:** A dynamic tiling window manager offering extensive customization. 
- **Qtile:** A highly configurable tiling window manager written in Python.

This was created in an Arcolinux offline setup vía the [Arconet ISO](https://www.arcolinux.info/downloads/). 

### Install dependencies

First, install the required packages:

       yay -S alacritty anyrun-git btop copyq fastfetch foot fuzzel grimblast hypridle hyprland hyprlock hyprpicker lib32-pipewire libnotify niri nmtui pipewire playerctl polkit-gnome pyprland qtile rofi ruby-fusuma swayidle swaylock swaync swayosd-git swww sxhkd thunar volumectl waybar wldash wl-clipboard wlogout wlsunset wireplumber wlr-protocols wttr wttrbar xwayland-satellite xfce4-appfinder yad
       
#### Replace PulseAudio with PipeWire

This configuration utilizes PipeWire for audio management. If you prefer to use PulseAudio, modify the `waybar` configuration to use the `pulseaudio` module instead of the `wireplumber` module.

1. Remove PulseAudio:
  
       sudo pacman -R pulseaudio-alsa pulseaudio-bluetooth pulseaudio jack2

2. Install PipeWire:

       sudo pacman -S pipewire-alsa pipewire-jack lib32-pipewire-jack wireplumber pipewire-zeroconf pipewire-pulse gnome-bluetooth blueman
  
#### Configuring Fusuma for Qtile

To configure [Fusuma](https://github.com/iberianpig/fusuma) for use with Qtile, follow this guide:

[How to Install and Customize Fusuma](https://dev.to/iberianpig/how-to-install-and-customize-fusuma-73l) 

This guide provides detailed instructions on:

* Installing Fusuma
* Configuring gestures for your touchpad
* Customizing actions for each gesture
* Integrating Fusuma with Qtile

By following the steps outlined in the guide, you can set up and customize `fusuma` to switch your Qtile wokspaces using touchpad gestures.

## Installation

1. Clone the repository:

       git clone https://github.com/arqueon/niri_hypr_qtile.git

2. Copy the desired configuration files to your `$HOME` directory.

3. Restart your window manager or log out and back in.

## Customization

Feel free to modify the configuration files to suit your preferences. Refer to the documentation for each tool for detailed customization options. You are welcome to fork this configuration files. Do not install in a production environment before testing and customizing. 

This configuration is a starting point. You're encouraged to personalize it to match your workflow and aesthetic preferences.  

Here's how:

* **Explore the Configuration Files:** Dive into the various configuration files located in this repository. Each file controls a different aspect of the setup, allowing for granular customization.
* **Consult the Documentation:** For detailed explanations and advanced options, refer to the official documentation for each tool:
    *   [Niri](https://github.com/YaLTeR/niri/wiki/Getting-Started)
    *   [Hyprland](https://wiki.hyprland.org/)
    *   [Qtile](https://docs.qtile.org/en/latest/)
* **Fork and Experiment:** Feel free to fork this repository and experiment with different settings. This allows you to safely test changes without affecting your main configuration.

**Important Note:** It is strongly recommended to thoroughly test any modifications in a non-production environment before applying them to your primary system.
