# Justine Smithies
# https://github.com/justinesmithies/qtile-wayland-dotfiles

# Groups configuration

from libqtile.config import Key, Group
from libqtile.command import lazy
from keys import mod, keys
from workspaces import workspaces
from screens import connected_monitors
from libqtile.config import ScratchPad, DropDown
from os import environ

# Get terminal from environment variables
terminal = environ.get("TERMINAL")

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    layouts = workspace["layout"] if "layout" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=layouts))
    keys.append(Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen()))
    keys.append(Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"])))

for i in range(connected_monitors):
    keys.extend([Key([mod, "mod1"], str(i), lazy.window.toscreen(i))])

# Append a scratchpad group

conf = {
    "warp_pointer": False,
    "on_focus_lost_hide": False,
    "opacity": 0.80,
}

groups.append(
    ScratchPad(
        "scratchpad", [
            # Define a drop down terminal
            # it is placed in the upper third of the screen by default
            DropDown(
                "term",
                terminal + " --class='Terminal'",
                height=0.50,
                width=0.50,
                x=0.25,
                y=0.2,
                **conf
            ),

        ]
    )
)

# Define keys to toggle the dropdown terminals
keys.extend([
    Key([mod, "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle("term")),
])
