# Niri, Hyprland and Qtile dotfiles for [ArcoLinux](https://www.arcolinux.info/)

## Niri
![image](https://github.com/user-attachments/assets/ca9bfc13-b453-450a-899a-0d72e327a4ae)
## Hyprland
![image](https://github.com/user-attachments/assets/586ee510-9e5d-485e-916f-d5025f872759)
## Qtile
![image](https://github.com/user-attachments/assets/643f8d4c-5871-42eb-a7fc-76ea33e45f36)

## Dependencies

This repository provides _dotfiles_ for a customized desktop environment on [ArcoLinux](https://www.arcolinux.info/), featuring the [Niri](https://github.com/YaLTeR/niri) compositor, [Hyprland](https://github.com/hyprwm/Hyprland) and [Qtile](https://github.com/qtile/qtile) window managers.

- **Niri:** A Wayland compositor known for its performance and minimalist design, inspired in PaperWM. 
- **Hyprland:** A dynamic tiling window manager offering extensive customization. 
- **Qtile:** A highly configurable tiling window manager written in Python.

This was created in an Arcolinux offline setup vía the [Arconet ISO](https://www.arcolinux.info/downloads/). 

### Install dependencies

First, install the required packages:

    yay -S alacritty anyrun-git btop catppuccin-gtk-theme-macchiato copyq curl fastfetch foot fuzzel git grimblast hypridle hyprland hyprlock hyprpicker kvantum-theme-catppuccin-git lib32-pipewire libnotify niri nmtui nwg-bar nwg-drawer nwg-look papirus-icon-theme papirus-folders-catppuccin-git pipewire playerctl pokemon-colorscripts-git polkit-gnome pyprland qt5ct qt6ct qtile rofi ruby-fusuma swayidle swaylock swaync swayosd-git swww sxhkd thunar volumectl waybar wldash wl-clipboard wlogout wlsunset wireplumber wl- clipboard wlr-protocols wttr wttrbar xwayland-satellite xfce4-appfinder yad 

#### Replace PulseAudio with PipeWire

This configuration utilizes PipeWire for audio management. If you prefer to use PulseAudio, modify the `waybar` configuration to use the `pulseaudio` module instead of the `wireplumber` module.

1. Remove PulseAudio:

       sudo pacman -Rdd pulseaudio

2. Install PipeWire:
 
       sudo pacman -S pipewire-{jack,alsa,pulse}
       systemctl --user enable --now pipewire pipewire-pulse 
  
#### More configurations

##### Configure `papirus-folders` for catppuccin machiatto green

    papirus-folders -C cat-macchiato-green -t Papirus-Dark

##### Install fonts

    pacman -S awesome-terminal-fonts --noconfirm --needed
    pacman -S nerd-fonts-source-code-pro --noconfirm --needed
    noto-fonts is already installed - nothing to do
    pacman -S ttf-iosevka-nerd --noconfirm --needed
    pacman -S ttf-jetbrains-mono --noconfirm --needed
    pacman -S ttf-nerd-fonts-symbols --noconfirm --needed
    pacman -S ttf-nerd-fonts-symbols-mono --noconfirm --needed
    yay -S --noconfirm ttf-meslo-nerd-font-powerlevel10k

##### Install and configure `zsh` 

    pacman -S zsh-completions --noconfirm --needed
    pacman -S zsh-autosuggestions --noconfirm --needed
    pacman -S zsh-syntax-highlighting --noconfirm --needed
    pacman -S oh-my-zsh-git --noconfirm --needed
    chsh -s /bin/zsh
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    yay -S --noconfirm zsh-theme-powerlevel10k-git
    echo 'source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc

#### Configuring Fusuma for Qtile (optional)

This setup integrates [Fusuma](https://github.com/iberianpig/fusuma), a versatile tool that enables you to control your Qtile environment using intuitive touchpad gestures. 

A functional configuration file (`fusuma/config.yml`) is already included in this repository. This provides a solid foundation for customization. You can modify this file to define your preferred gestures and actions, tailoring the experience to your specific needs.

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


## Configuration Customization. Make it your own!

This repository provides a minimal foundation for setting up your workspace with Niri and Hyprland. But don't stop there! Adapt it to your liking and needs.

### Here's how

* **Explore the configuration files:** Dive into the files within the repository. Each one controls a specific aspect, allowing for granular customization.

* **Consult the documentation:** For advanced options and detailed explanations, check out the official documentation for each tool:

  * [Niri](https://github.com/YaLTeR/niri/wiki/Getting-Started): A powerful window manager with a minimalist approach.
  * [Hyprland](https://wiki.hyprland.org/): A highly customizable Wayland compositor that gives you complete control over your graphical environment.
  * [Qtile](https://docs.qtile.org/en/latest/): If you prefer a dynamic window manager, Qtile offers flexibility and extensibility.

* **Fork and experiment:** Create your own copy of the repository (fork) and experiment with different settings. This allows you to safely test changes without affecting your main configuration.

**Important!** Test any modifications in a test environment before applying them to your main system.

### Essential adjustments

For an optimal experience, you'll need to adjust the input and output settings for Niri and Hyprland:

#### Niri

* **Input:**

  * Change your keyboard configuration. 
  * Map your favorite keys to specific actions. Explore options like keyboard shortcuts to launch applications, switch between workspaces, or control volume.
  * Configure your touchpad for gestures, scrolling, and sensitivity.

* **Output:**

  * Define the layout of your monitors, resolution, and scaling.
  * Customize the appearance of Niri with themes, colors, and fonts.

#### Hyprland

* **Input:**
  
  * Change your keyboard configuration. 
  * Configure keyboard shortcuts for window management, workspaces, and other actions. Hyprland offers great flexibility to create an efficient workflow.
  * Adjust mouse sensitivity and acceleration.

* **Output:**

  * Define the layout of your monitors, including position, resolution, and scaling.
  * Customize the appearance with themes, window borders, shadows, and animations.

Feel free to explore and customize your environment until it's perfect for you!

### Important Note

It is **highly recommended** to test any modifications in a non-production environment before applying them to your main system. This ensures that all changes are safe and functional.

Feel free to experiment and personalize this configuration to perfectly match your workflow!


### ArcoLinux Tweak Tool (ATT)

[ArcoLinux Tweak Tool (ATT)](https://arcolinux.com/everything-you-need-to-know-about-the-arcolinux-tweak-tool/) is a versatile and powerful tool designed to simplify the customization of Arch-based systems. It can help you:

* **Easily personalize your desktop environment.**
* **Troubleshoot and fix common issues.**
* **Install a wide variety of desktop environments and window managers.**

ATT provides a user-friendly interface for managing various aspects of your system, making it an invaluable tool for both new and experienced Arch users.

    yay -S archlinux-tweak-tool-git
## Keybinds

### Niri

| Category | Keybind | Action |
|---|---|---|
| **Launching** | `Mod+D` |  Launch Fuzzel (application launcher) |
|  | `Mod+Return` | Launch Alacritty (terminal emulator) |
|  | `Mod+Space` | Launch Anyrun | 
|  | `Mod+period` | Launch Anyrun |
|  | `Mod+Shift+Return` | Launch Thunar (file manager) |
|  | `Mod+F1` | Launch Google Chrome |
|  | `Mod+F2` | Launch Ferdium |
|  | `Mod+F3` | Launch Zotero |
|  | `Mod+F4` | Launch Logseq |
|  | `Mod+F5` | Launch Zettlr |
|  | `Mod+F6` | Launch Doublecmd |
|  | `Mod+F7` | Launch Virt-manager |
|  | `Mod+F8` | Launch Qbittorrent |
|  | `Mod+F9` | Launch Jdownloader |
|  | `Mod+F10` | Launch Youtube-music |
|  | `Mod+F11` | Launch MPV (to `/dev/video2`) |
|  | `Mod+F12` | Launch Wldash |
|  | `Mod+Shift+C` | Launch Guvcview |

| **Window Management** | Keybind | Action |
|---|---|---|
| **Focus** | `Mod+Left` | Focus column to the left |
|  | `Mod+Down` | Focus window or workspace down |
|  | `Mod+Up` | Focus window or workspace up |
|  | `Mod+Right` | Focus column to the right |
|  | `Mod+Home` | Focus first column |
|  | `Mod+End` | Focus last column |
| **Move** | `Mod+Ctrl+Left` | Move column left |
|  | `Mod+Ctrl+Down` | Move window down |
|  | `Mod+Ctrl+Up` | Move window up |
|  | `Mod+Ctrl+Right` | Move column right |
|  | `Mod+Ctrl+H` | Move column left |
|  | `Mod+Ctrl+J` | Move window down |
|  | `Mod+Ctrl+K` | Move window up |
|  | `Mod+Ctrl+L` | Move column right |
|  | `Mod+Ctrl+Home` | Move column to first position |
|  | `Mod+Ctrl+End` | Move column to last position |
| **Resize** | `Mod+R` | Switch preset column width |
|  | `Mod+Shift+R` | Reset window height |
|  | `Mod+Minus` | Decrease column width |
|  | `Mod+Equal` | Increase column width |
|  | `Mod+Shift+Minus` | Decrease window height |
|  | `Mod+Shift+Equal` | Increase window height |
| **Other** |  `Mod+Q` | Close window |
|  | `Mod+I` | Consume window into column |
|  | `Mod+O` | Expel window from column |
|  | `Mod+BracketLeft` | Consume or expel window left |
|  | `Mod+BracketRight` | Consume or expel window right |
|  | `Mod+F` | Maximize column |
|  | `Mod+Shift+F` | Fullscreen window |
|  | `Mod+C` | Center column |

| **Workspace Management** | Keybind | Action |
|---|---|---|
| **Focus** | `Mod+Page_Down` | Focus workspace down |
|  | `Mod+Page_Up` | Focus workspace up |
|  | `Mod+1` | Focus workspace 1 |
|  | `Mod+2` | Focus workspace 2 |
|  | `Mod+3` | Focus workspace 3 |
|  | `Mod+4` | Focus workspace 4 |
|  | `Mod+5` | Focus workspace 5 |
|  | `Mod+6` | Focus workspace 6 |
|  | `Mod+7` | Focus workspace 7 |
|  | `Mod+8` | Focus workspace 8 |
|  | `Mod+9` | Focus workspace 9 |
|  | `Mod+Tab` | Focus previous workspace |
| **Move** | `Mod+Ctrl+Page_Down` | Move column to workspace down |
|  | `Mod+Ctrl+Page_Up` | Move column to workspace up |
|  | `Mod+Ctrl+U` | Move column to workspace down |
|  | `Mod+Ctrl+I` | Move column to workspace up |
|  | `Mod+Shift+Page_Down` | Move workspace down |
|  | `Mod+Shift+Page_Up` | Move workspace up |
|  | `Mod+Shift+U` | Move workspace down |
|  | `Mod+Shift+I` | Move workspace up |
|  | `Mod+Shift+1` | Move column to workspace 1 |
|  | `Mod+Shift+2` | Move column to workspace 2 |
|  | `Mod+Shift+3` | Move column to workspace 3 |
|  | `Mod+Shift+4` | Move column to workspace 4 |
|  | `Mod+Shift+5` | Move column to workspace 5 |
|  | `Mod+Shift+6` | Move column to workspace 6 |
|  | `Mod+Shift+7` | Move column to workspace 7 |
|  | `Mod+Shift+8` | Move column to workspace 8 |
|  | `Mod+Shift+9` | Move column to workspace 9 |

| **Monitor Management** | Keybind | Action |
|---|---|---|
| **Focus** | `Mod+Shift+Left` | Focus monitor to the left |
|  | `Mod+Shift+Down` | Focus monitor down |
|  | `Mod+Shift+Up` | Focus monitor up |
|  | `Mod+Shift+Right` | Focus monitor to the right |
| **Move** | `Mod+Shift+Ctrl+Left` | Move column to monitor on the left |
|  | `Mod+Shift+Ctrl+Down` | Move column to monitor down |
|  | `Mod+Shift+Ctrl+Up` | Move column to monitor up |
|  | `Mod+Shift+Ctrl+Right` | Move column to monitor on the right |
|  | `Mod+Alt+Ctrl+Left` | Move workspace to monitor on the left |
|  | `Mod+Alt+Ctrl+Right` | Move workspace to monitor on the right |

| **System** | Keybind | Action |
|---|---|---|
|  | `Mod+Shift+Slash` | Show hotkey overlay |
|  | `Ctrl+Alt+Escape` |  Launch screen locker script |
|  | `Mod+L` | Launch screen locker script |
|  | `Mod+X` | Launch nwg-bar |
|  | `Mod+Z` | Restart xwayland-satellite | 
|  | `Mod+Escape` | Launch btop |
|  | `Mod+Shift+W` | Launch Waybar script |
|  | `XF86AudioLowerVolume` | Lower volume |
|  | `XF86AudioMute` | Toggle mute |
|  | `XF86AudioRaiseVolume` | Raise Volume |
|  | `XF86MonBrightnessDown` | Decrease brightness |
|  | `XF86MonBrightnessUp` | Increase brightness |
|  | `F11` | Lower volume |
|  | `F10` | Toggle mute |
|  | `F12` | Raise volume |
|  | `Print` | Take screenshot |
|  | `Ctrl+Print` | Take screenshot of screen |
|  | `Alt+Print` | Take screenshot of window |
|  | `Mod+Shift+E` | Exit Niri |
|  | `Mod+Shift+P` | Power off monitors |

**Notes:**

*  `Mod` is usually the Super key (Windows key).
*  Remember that you can further customize these binds or add new ones in your `config.kdl` file.

### Hyprland 

| Category | Keybind | Action |
|---|---|---|
| **Launching** | `$mainMod, Return` | Launch Alacritty (terminal) |
|  | `$mainMod SHIFT, Return` | Launch Thunar (file manager) |
|  | `$mainMod, D` | Launch dmenu  |
|  | `$mainMod, B` | Launch librewolf (browser) |
|  | `$mainMod SHIFT, B` | Launch Google Chrome |
|  | `$mainMod, E` | Launch Thunar |
|  | `$mainMod SHIFT, P` | Launch passmenu |
|  | `$mainMod, F1` | Launch Google Chrome |
|  | `$mainMod, F2` | Launch Ferdium |
|  | `$mainMod, F3` | Launch Zotero |
|  | `$mainMod, F4` | Launch Logseq |
|  | `$mainMod, F5` | Launch Zettlr |
|  | `$mainMod, F6` | Launch Doublecmd |
|  | `$mainMod, F7` | Launch Virt-manager |
|  | `$mainMod, F8` | Launch Qbittorrent |
|  | `$mainMod, F9` | Launch Jdownloader |
|  | `$mainMod, F10` | Launch Youtube-music |
|  | `$mainMod, F11` | Launch Kamoso |
|  | `$mainMod, F12` | Launch Pamac-manager |
|  | `ALT, F3` | Launch xfce4-appfinder |
|  | `CTRL ALT, P` | Launch Pamac-manager |
|  | `$mainMod, Space` | Launch Rofi |


| **Window Management** | Keybind | Action |
|---|---|---|
| **Focus** | `$mainMod, left` | Move focus left |
|  | `$mainMod, right` | Move focus right |
|  | `$mainMod, up` | Move focus up |
|  | `$mainMod, down` | Move focus down |
|  | `$mainMod, H` | Move focus left |
|  | `$mainMod, L` | Move focus right |
|  | `$mainMod, K` | Move focus up |
|  | `$mainMod, J` | Move focus down |
| **Move** | `$mainMod SHIFT, left` | Move window left |
|  | `$mainMod SHIFT, right` | Move window right |
|  | `$mainMod SHIFT, up` | Move window up |
|  | `$mainMod SHIFT, down` | Move window down |
|  | `$mainMod SHIFT, H` | Move window left |
|  | `$mainMod SHIFT, L` | Move window right |
|  | `$mainMod SHIFT, K` | Move window up |
|  | `$mainMod SHIFT, J` | Move window down |
| **Resize** | `$mainMod, R` | Enter resize submap |
|  | (in resize submap) `, right` | Resize active window right |
|  | (in resize submap) `, left` | Resize active window left |
|  | (in resize submap) `, up` | Resize active window up |
|  | (in resize submap) `, down` | Resize active window down |
|  | (in resize submap) `, l` | Resize active window right |
|  | (in resize submap) `, h` | Resize active window left |
|  | (in resize submap) `, k` | Resize active window up |
|  | (in resize submap) `, j` | Resize active window down |
|  | (in resize submap) `, escape` | Exit resize submap |
|  | `$mainMod, R` | Exit resize submap |
| **Other** | `$mainMod, Q` | Kill active window |
|  | `$mainMod SHIFT, A` | Toggle floating |
|  | `$mainMod, F` | Fullscreen |
|  | `$mainMod, C` | Center window |
|  | `$mainMod CTRL, P` | Pin window |
|  | `$mainMod, P` | Enter pseudo-tile mode |


| **Workspace Management** | Keybind | Action |
|---|---|---|
| **Focus** | `$mainMod, 1` | Focus workspace 1 |
|  | `$mainMod, 2` | Focus workspace 2 |
|  | `$mainMod, 3` | Focus workspace 3 |
|  | `$mainMod, 4` | Focus workspace 4 |
|  | `$mainMod, 5` | Focus workspace 5 |
|  | `$mainMod, 6` | Focus workspace 6 |
|  | `$mainMod, 7` | Focus workspace 7 |
|  | `$mainMod, 8` | Focus workspace 8 |
|  | `$mainMod, 9` | Focus workspace 9 |
|  | `$mainMod, 0` | Focus workspace 10 |
|  | `$mainMod, mouse_down` | Focus next workspace |
|  | `$mainMod, mouse_up` | Focus previous workspace |
|  | `$mainMod CTRL, left` | Change workspace +1 (using Pyprland) |
|  | `$mainMod CTRL, right` | Change workspace -1 (using Pyprland) |
| **Move** | `$mainMod SHIFT, 1` | Move to workspace 1 |
|  | `$mainMod SHIFT, 2` | Move to workspace 2 |
|  | `$mainMod SHIFT, 3` | Move to workspace 3 |
|  | `$mainMod SHIFT, 4` | Move to workspace 4 |
|  | `$mainMod SHIFT, 5` | Move to workspace 5 |
|  | `$mainMod SHIFT, 6` | Move to workspace 6 |
|  | `$mainMod SHIFT, 7` | Move to workspace 7 |
|  | `$mainMod SHIFT, 8` | Move to workspace 8 |
|  | `$mainMod SHIFT, 9` | Move to workspace 9 |
|  | `$mainMod SHIFT, 0` | Move to workspace 10 |
| **Other** | `$mainMod SHIFT, MINUS` | Move to special workspace |
|  | `$mainMod, MINUS` | Toggle special workspace |

| **System** | Keybind | Action |
|---|---|---|
| **Audio** | `XF86AudioRaiseVolume` | Increase volume |
|  | `XF86AudioLowerVolume` | Decrease volume |
|  | `XF86AudioMute` | Toggle mute |
|  | `$mainMod SHIFT, O` | Toggle mute |
|  | `XF86AudioMicMute` | Toggle microphone mute |
|  | `$mainMod SHIFT, M` | Toggle microphone mute |
|  | `F10` | Toggle mute |
|  | `F11` | Decrease volume |
|  | `F12` | Increase volume |
| **Brightness** | `XF86MonBrightnessUp` | Increase brightness |
|  | `XF86MonBrightnessDown` | Decrease brightness |
| **Screenshots** | `$mainMod SHIFT, S` | Copy area screenshot |
|  | `$mainMod SHIFT CTRL, S` | Save area screenshot |
|  | `$mainMod, Print` | Copy area screenshot |
|  | `$mainMod SHIFT, X` | Copy output screenshot |
|  | `$mainMod SHIFT CTRL, X` | Save output screenshot |
| **Other** | `$mainMod SHIFT, Delete` | Exit Hyprland |
|  | `$mainMod SHIFT, C` | Copy color under cursor |
|  | `$mainMod SHIFT, R` | Start screen recording |
|  | `$mainMod, V` | Toggle CopyQ |
|  | `$mainMod SHIFT, Q` | Run system action script |
|  | `$mainMod ALT, L` | Pause player and lock screen |
|  | `$mainMod, L` | Lock screen |
|  | `$mainMod, X` | Launch wlogout |
|  | `$mainMod SHIFT, W` | Launch Waybar script |
|  | `$mainMod SHIFT, I` | Shift monitors (using Pyprland) |
|  | `$mainMod ALT, P` | Toggle DPMS (using Pyprland) |
|  | `$mainMod SHIFT, T` | Toggle dropdown terminal (using Pyprland) |
|  | `$mainMod, Z` | Toggle zoom (using Pyprland) |

**Notes:**

* `$mainMod` is your main modifier key, which you define in your Hyprland configuration.
* This table omits the mouse button binds for moving and resizing windows.
* Some functionalities are achieved through external scripts or programs.
* You can always customize or add more keybinds in your Hyprland configuration file.

### Qtile 

From a mix of Qtile (from `config.py`) and `sxhkd` keybinds.

| Category | Keybind | Action | Source |
|---|---|---|---|
| **Launching** | `super + F1` | Launch Google Chrome | sxhkd |
|  | `super + F2` | Launch Ferdium | sxhkd |
|  | `super + F3` | Launch Zotero | sxhkd |
|  | `super + F4` | Launch Logseq | sxhkd |
|  | `super + F5` | Launch Zettlr | sxhkd |
|  | `super + F6` | Launch Doublecmd | sxhkd |
|  | `super + F7` | Launch Virt-manager | sxhkd |
|  | `super + F8` | Launch Qbittorrent | sxhkd |
|  | `super + F9` | Launch Jdownloader | sxhkd |
|  | `super + F10` | Toggle audio mute | sxhkd |
|  | `super + F11` | Decrease volume | sxhkd |
|  | `super + F12` | Increase volume | sxhkd |
|  | `super + e` | Launch Geany | sxhkd |
|  | `super + w` | Launch Google Chrome | sxhkd |
|  | `super + ctrl + c` | Kill all Conky processes | sxhkd |
|  | `super + x` | Launch archlinux-logout | sxhkd |
|  | `super + r` | Launch rofi-theme-selector | sxhkd |
|  | `super + t` | Launch urxvt | sxhkd |
|  | `super + v` | Launch pavucontrol | sxhkd |
|  | `super + Return` | Launch alacritty | sxhkd |
|  | `super + Escape` | Launch xkill | sxhkd |
|  | `super + KP_Enter` | Launch alacritty | sxhkd |
|  | `super + shift + Return` | Launch Thunar | sxhkd |
|  | `super + shift + d` | Launch dmenu_run | sxhkd |
|  | `ctrl + alt + w` | Launch arcolinux-welcome-app | sxhkd |
|  | `ctrl + alt + e` | Launch archlinux-tweak-tool | sxhkd |
|  | `ctrl + alt + b` | Launch Thunar | sxhkd |
|  | `ctrl + alt + c` | Launch Catfish | sxhkd |
|  | `ctrl + alt + g` | Launch Chromium | sxhkd |
|  | `ctrl + alt + f` | Launch Firefox | sxhkd |
|  | `ctrl + alt + i` | Launch Nitrogen | sxhkd |
|  | `ctrl + alt + k` | Launch archlinux-logout | sxhkd |
|  | `ctrl + alt + l` | Launch archlinux-logout | sxhkd |
|  | `ctrl + alt + p` | Launch Pamac-manager | sxhkd |
|  | `ctrl + alt + m` | Launch xfce4-settings-manager | sxhkd |
|  | `ctrl + alt + u` | Launch pavucontrol | sxhkd |
|  | `ctrl + alt + r` | Launch rofi-theme-selector | sxhkd |
|  | `ctrl + alt + s` | Launch Spotify | sxhkd |
|  | `ctrl + alt + Return` | Launch alacritty | sxhkd |
|  | `ctrl + alt + t` | Launch alacritty | sxhkd |
|  | `ctrl + alt + v` | Launch Google Chrome | sxhkd |
|  | `ctrl + alt + a` | Launch xfce4-appfinder | sxhkd |
|  | `alt + F2` | Launch xfce4-appfinder (collapsed) | sxhkd |
|  | `alt + F3` | Launch xfce4-appfinder | sxhkd |
|  | `ctrl + shift + Escape` | Launch xfce4-taskmanager | sxhkd |
|  | `ctrl + Print` | Launch xfce4-screenshooter | sxhkd |
|  | `ctrl + shift + Print` | Launch gnome-screenshot | sxhkd |
|  | `ctrl + alt + o` | Launch picom-toggle.sh | sxhkd |
|  | `mod, Return` | Launch alacritty | Qtile |

| **Window Management** | Keybind | Action | Source |
|---|---|---|---|
| **Focus** | `mod + Up` | Focus window above | Qtile |
|  | `mod + Down` | Focus window below | Qtile |
|  | `mod + Left` | Focus window on the left | Qtile |
|  | `mod + Right` | Focus window on the right | Qtile |
|  | `mod + k` | Focus window above | Qtile |
|  | `mod + j` | Focus window below | Qtile |
|  | `mod + h` | Focus window on the left | Qtile |
|  | `mod + l` | Focus window on the right | Qtile |
| **Move** | `mod + shift + Up` | Shuffle window up | Qtile |
|  | `mod + shift + Down` | Shuffle window down | Qtile |
|  | `mod + shift + Left` | Swap window left | Qtile |
|  | `mod + shift + Right` | Swap window right | Qtile |
|  | `mod + shift + k` | Shuffle window up | Qtile |
|  | `mod + shift + j` | Shuffle window down | Qtile |
|  | `mod + shift + h` | Swap window left | Qtile |
|  | `mod + shift + l` | Swap window right | Qtile |
| **Resize** | `mod + control + h` | Increase window size to the left | Qtile |
|  | `mod + control + Right` | Increase window size to the right | Qtile |
|  | `mod + control + l` | Decrease window size to the right | Qtile |
|  | `mod + control + Left` | Decrease window size to the left | Qtile |
|  | `mod + control + k` | Increase window size upwards | Qtile |
|  | `mod + control + Up` | Increase window size upwards | Qtile |
|  | `mod + control + j` | Decrease window size downwards | Qtile |
|  | `mod + control + Down` | Decrease window size downwards | Qtile |
| **Other** | `mod + f` | Toggle fullscreen | Qtile |
|  | `mod + q` | Close window | Qtile |
|  | `mod + shift + space` | Toggle floating | Qtile |


| **Workspace Management** | Keybind | Action | Source |
|---|---|---|---|
| **Focus** | `mod + 1` | Focus group 1 | Qtile |
|  | `mod + 2` | Focus group 2 | Qtile |
|  | `mod + 3` | Focus group 3 | Qtile |
|  | `mod + 4` | Focus group 4 | Qtile |
|  | `mod + 5` | Focus group 5 | Qtile |
|  | `mod + 6` | Focus group 6 | Qtile |
|  | `mod + 7` | Focus group 7 | Qtile |
|  | `mod + 8` | Focus group 8 | Qtile |
|  | `mod + 9` | Focus group 9 | Qtile |
|  | `mod + 0` | Focus group 10 | Qtile |
|  | `mod + minus` | Focus group 11 | Qtile |
|  | `mod + equal` | Focus group 12 | Qtile |
|  | `mod1 + Tab` | Focus next group | Qtile |
|  | `mod1 + shift + Tab` | Focus previous group | Qtile |
| **Move** | `mod + shift + 1` | Move to group 1 | Qtile |
|  | `mod + shift + 2` | Move to group 2 | Qtile |
|  | `mod + shift + 3` | Move to group 3 | Qtile |
|  | `mod + shift + 4` | Move to group 4 | Qtile |
|  | `mod + shift + 5` | Move to group 5 | Qtile |
|  | `mod + shift + 6` | Move to group 6 | Qtile |
|  | `mod + shift + 7` | Move to group 7 | Qtile |
|  | `mod + shift + 8` | Move to group 8 | Qtile |
|  | `mod + shift + 9` | Move to group 9 | Qtile |
|  | `mod + shift + 0` | Move to group 10 | Qtile |
|  | `mod + shift + minus` | Move to group 11 | Qtile |
|  | `mod + shift + equal` | Move to group 12 | Qtile |

| **Monitor Management** | Keybind | Action | Source |
|---|---|---|---|
| **Focus** | `mod + i` | Focus monitor 1 | Qtile |
|  | `mod + o` | Focus monitor 2 | Qtile |
|  | `mod + period` | Focus next monitor | Qtile |
|  | `mod + comma` | Focus previous monitor | Qtile |
| **Move** | `mod + shift + Right` | Move window to next monitor | Qtile |
|  | `mod + shift + Left` | Move window to previous monitor | Qtile |

| **System** | Keybind | Action | Source |
|---|---|---|---|
| **Qtile** | `mod + shift + r` | Restart Qtile | Qtile |
|  | `mod + shift + x` | Shutdown Qtile | Qtile |
|  | `mod + r` | Reset layout | Qtile |
|  | `mod + Tab` | Next layout | Qtile |
|  | `mod + shift + f` | Flip layout | Qtile |
| **sxhkd** | `super + shift + s` | Reload sxhkd | sxhkd |
|  | `alt + t` | Move wallpaper to trash | sxhkd |
|  | `alt + n` | Next wallpaper | sxhkd |
|  | `alt + p` | Previous wallpaper | sxhkd |
|  | `alt + f` | Favorite wallpaper | sxhkd |
|  | `alt + Left` | Previous wallpaper | sxhkd |
|  | `alt + Right` | Next wallpaper | sxhkd |
|  | `alt + Up` | Toggle pause wallpaper | sxhkd |
|  | `alt + Down` | Resume wallpaper | sxhkd |
|  | `alt + shift + t` | Trash wallpaper and update pywal | sxhkd |
|  | `alt + shift + n` | Next wallpaper and update pywal | sxhkd |
|  | `alt + shift + p` | Previous wallpaper and update pywal | sxhkd |
|  | `alt + shift + f` | Favorite wallpaper and update pywal | sxhkd |
|  | `alt + shift + u` | Update pywal | sxhkd |
|  | `Print` | Take screenshot with scrot | sxhkd |
|  | `XF86AudioRaiseVolume` | Increase volume | sxhkd |
|  | `XF86AudioLowerVolume` | Decrease volume | sxhkd |
|  | `XF86AudioMute` | Toggle mute | sxhkd |
|  | `XF86AudioPlay` | Play/pause (playerctl) | sxhkd |
|  | `XF86AudioNext` | Next track (playerctl) | sxhkd |
|  | `XF86AudioPrev` | Previous track (playerctl) | sxhkd |
|  | `XF86AudioStop` | Stop (playerctl) | sxhkd |
|  | `XF86MonBrightnessUp` | Increase brightness | sxhkd |
|  | `XF86MonBrightnessDown` | Decrease brightness | sxhkd |

**Notes:**

* `super` is the Super key (Windows key).
* `mod` is `mod4`, which is also the Super key.
* `mod1` is `Alt`.
* This table combines keybinds from both Qtile `config.py` and sxhkd configuration.
* Some actions are handled by external scripts.
* You can customize or add more keybinds in your respective configuration files.

