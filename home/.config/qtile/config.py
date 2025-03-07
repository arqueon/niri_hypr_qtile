
from typing import List  # noqa: F401
import os
import subprocess
from os import path

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen
from libqtile.lazy import lazy
from settings.path import qtile_path
import colors

mod = "mod4"
terminal = "alacritty"

keys = [
    # Open terminal
    Key([mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"),

    # Qtile System Actions
    Key([mod, "shift"], "r", lazy.restart(),
        desc="Restart Qtile"),
    Key([mod, "shift"], "x", lazy.shutdown(),
        desc="Shutdown Qtile"),

    # Active Window Actions
    Key([mod], "f", lazy.window.toggle_fullscreen(), 
        desc="Toggle window fullscreen"),
    Key([mod], "q", lazy.window.kill(), 
        desc="Close active window"),
    Key([mod, "control"], "h",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size."
        ),

    # Window Focus (Arrows and Vim keys)
    Key([mod], "Up", lazy.layout.up(),
        desc="Change focus to window above."),
    Key([mod], "Down", lazy.layout.down(),
        desc="Change focus to window below."),
    Key([mod], "Left", lazy.layout.left(),
        desc="Change focus to window on the left."),
    Key([mod], "Right", lazy.layout.right(),
        desc="Change focus to window on the right."),
    Key([mod], "k", lazy.layout.up(),
        desc="Change focus to window above."),
    Key([mod], "j", lazy.layout.down(),
        desc="Change focus to window below."),
    Key([mod], "h", lazy.layout.left(),
        desc="Change focus to window on the left."),
    Key([mod], "l", lazy.layout.right(),
        desc="Change focus to window on the right."),

    # Qtile Layout Actions
    Key([mod], "r", lazy.layout.reset(),
        desc="Reset the sizes of all window in group."),
    Key([mod], "Tab", lazy.next_layout(),
        desc="Switch to the next layout."),
    Key([mod, "shift"], "f", lazy.layout.flip(),
        desc="Flip layout for Monadtall/Monadwide"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle floating window."),

    # Move windows around MonadTall/MonadWide Layouts
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Shuffle window up."),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Shuffle window down."),
    Key([mod, "shift"], "Left", lazy.layout.swap_left(),
        desc="Shuffle window left."),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(),
        desc="Shuffle window right."),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Shuffle window up."),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Shuffle window down."),
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Shuffle window left."),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Shuffle window right."),
    
    # Switch focus to specific monitor (out of three)
    Key([mod], "i",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'),
    Key([mod], "o",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'),

    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma",
        lazy.prev_scrSeen(),
        desc='Move focus to prev monitor'),
]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])


# Create labels for groups and assign them a default layout.
groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "minus", "equal"]

group_labels = ["", "", "", "", "", "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "", "", "", "", "", "ﭮ", "", "", "﨣"]
# group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadwide", "monadtall", "monadtall", "monadtall", "monadtall"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Mod + number to move to that group."),
        Key(["mod1"], "Tab", lazy.screen.next_group(),
            desc="Move to next group."),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(),
            desc="Move to previous group."),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to new group."),
    ])

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "alacritty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("ranger", "alacritty --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("volume", "alacritty --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("mus", "youtube-music", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("ferdium", "ferdium", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),

]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "c", lazy.group['scratchpad'].dropdown_toggle('yazi')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('mus')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('ferdium')),
])

colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.catppuccin()

# Define layouts and layout themes
layout_theme = {
        "margin":5,
        "border_width": 3,
        "border_focus": colors[4],
        "border_normal": backgroundColor
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

# Mouse callback functions
def launch_menu():
    qtile.cmd_spawn("rofi -show drun -show-icons")


# Define Widgets
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize = 12,
    padding = 2,
    background=backgroundColor
)

def init_widgets_list(monitor_num):
    widgets_list = [
        widget.GroupBox(
            font="JetBrainsMono Nerd Font",
            fontsize = 16,
            margin_y = 2,
            margin_x = 4,
            padding_y = 6,
            padding_x = 6,
            borderwidth = 2,
            disable_drag = True,
            active = colors[4],
            inactive = foregroundColor,
            hide_unused = False,
            rounded = False,
            highlight_method = "line",
            highlight_color = [backgroundColor, backgroundColor],
            this_current_screen_border = colors[5],
            this_screen_border = colors[7],
            other_screen_border = colors[6],
            other_current_screen_border = colors[6],
            urgent_alert_method = "line",
            urgent_border = colors[9],
            urgent_text = colors[1],
            foreground = foregroundColor,
            background = backgroundColor,
            use_mouse_wheel = False
        ),
        widget.TaskList(
            icon_size = 0,
            font = "JetBrainsMono Nerd Font",
            foreground = foregroundColor,
            background = colors[9],
            borderwidth = 2,
            border = colors[1],
            margin = 0,
            padding = 8,
            highlight_method = "block",
            title_width_method = "uniform",
            urgent_alert_method = "border",
            urgent_border = colors[1],
            rounded = False,
            txt_floating = "🗗 ",
            txt_maximized = "🗖 ",
            txt_minimized = "🗕 ",
        ),
        widget.Sep(
            linewidth = 1,
            padding = 10,
            foreground = colors[5],
            background = backgroundColor
        ),
        widget.OpenWeather(
            app_key = "eef70be9b67cd504291fc5b2319f40cd",
            cityid = "4005539",
            format = '{icon} {main_temp}°',
            metric = True,
            font = "JetBrainsMono Nerd Font",
            foreground = foregroundColor,
        ),
       widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.TextBox(
            text = " ",
            fontsize = 14,
            font = "JetBrainsMono Nerd Font",
            foreground = colors[7],
        ),
        widget.CPU(
            font = "JetBrainsMono Nerd Font",
            update_interval = 1.0,
            format = '{load_percent}%',
            foreground = foregroundColor,
            padding = 5
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.TextBox(
            text = "",
            fontsize = 14,
            font = "JetBrainsMono Nerd Font",
            foreground = colors[3],
        ),
        widget.Memory(
            font = "JetBrainsMonoNerdFont",
            foreground = foregroundColor,
            format = '{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}',
            measure_mem='G',
            padding = 5,
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.TextBox(
            text = " ",
            fontsize = 14,
            font = "JetBrainsMono Nerd Font",
            foreground = colors[10],
        ),
        widget.Clock(
            format='%d/%m/%y %H:%M',
            font = "JetBrainsMono Nerd Font",
            padding = 10,
            foreground = foregroundColor
        ),
        widget.Systray(
            background = backgroundColor,
            icon_size = 20,
            padding = 4,
        ),
        widget.Sep(
            linewidth = 1,
            padding = 10,
            foreground = colors[5],
            background = backgroundColor
        ),
        widget.CurrentLayoutIcon(
            scale = 0.5,
            foreground = foregroundColor,
            background = backgroundColor
        ),
    ]

    return widgets_list

def init_secondary_widgets_list(monitor_num):
    secondary_widgets_list = init_widgets_list(monitor_num)
    del secondary_widgets_list[13:14]
    return secondary_widgets_list

widgets_list = init_widgets_list("1")
secondary_widgets_list = init_secondary_widgets_list("2")
# secondary_widgets_list_2 = init_secondary_widgets_list("3")

# Define 3 monitors
screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=34,
            background=backgroundColor,
            margin=4, 
            opacity=0.8
        ),
    ),
    Screen(
        top=bar.Bar(
            widgets=secondary_widgets_list,
            size=34,
            background=backgroundColor,
            margin=4, 
            opacity=0.8
        ),
    ),
    # Screen(
    #     top=bar.Bar(
    #         widgets=secondary_widgets_list_2,
    #         size=36,
    #         background=backgroundColor,
    #         margin=6, 
    #         opacity=0.8
    #     ),
    # ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#Currently running Qtile in XFCE, so autostart script isn't necessary.  Uncomment if needed.
#Startup applications
@hook.subscribe.startup_once
def autostart():
   home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
   subprocess.run([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Mailspring'), # Mail client
], fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
# focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
#"Qtile 0.21.0"
