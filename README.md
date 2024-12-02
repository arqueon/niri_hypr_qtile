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
Customize this keybinds as you like in `config.kdl`. 

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
