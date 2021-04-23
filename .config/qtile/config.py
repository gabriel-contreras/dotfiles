# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

import os
import subprocess
import socket

mod = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('/.config/qtile/autostart.sh')
    subprocess.call([home])


### KEY BINDINGS ###
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Maximize focused window"),

    # Launch the Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Close the window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Firefox
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),

    # File Explorer
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Launch File Explorer"),

    # Zoom
    Key([mod], "z", lazy.spawn("zoom"), desc="Launch Zoom"),

    # Slack
    Key([mod], "s", lazy.spawn("slack"), desc="Launch Slack"),

    # Notion Notes app
    Key([mod], "n", lazy.spawn("notion-app"), desc="Launch Notion"),

    # Spotify
    Key([mod], "m", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([], "XF86AudioPlay", lazy.spawn(
        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioNext", lazy.spawn(
        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn(
        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer -c 0 sset Master 2- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer -c 0 sset Master 2+ unmute")),

    # Brightness (Cheap/Ugly way for now, fix this later!!)
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo light -U 10"))
]

### GROUPS (Desktops) ###
group_names = ["WWW", "CODE", "QNTM", "NOTES", "DOC", "CHAT", "MUS", "ZOOM"]
groups = [Group(name) for name in group_names]

for i, (name) in enumerate(group_names):
    keys.extend([
        # mod + number of group = switch to group
        Key([mod], str(i+1), lazy.group[name].toscreen(),
            desc="Switch to group {}".format(i+1)),

        # mod + shift + number of group = switch to & move focused window to group
        Key([mod, "shift"], str(i+1), lazy.window.toGroup(name),
            desc="Switch to & move focused window to group {}".format(i+1))
    ])

### LAYOUTS ###

layouts = [
    layout.MonadTall(
        border_focus="#5b6464",
        border_width=4,
        margin=10,
        single_margin=14
    ),
    # layout.TreeTab(
    #     active_bg = "#5597C4",
    #     active_fg = "#F7BB26",
    #     bg_color = "#A5B3B9",
    #     border_width = 4,
    #     font = "roman",
    #     fontshadow = "#000000",
    #     fontsize = 14,
    #     inactive_bg = "#6B7275",
    #     inactive_fg = "#FFFFFF",
    #     margin_left = 10,
    #     margin_y = 10,
    #     padding_left = 0,
    #     padding_x = 0,
    #     padding_y = 5,
    #     panel_width = 200,
    #     sections = ['Tabs'],
    #     section_bottom = 5,
    #     section_top = 5,
    #     section_fg = "#2293C1",
    #     section_fontsize = 16,
    #     section_left = 5,
    #     section_padding = 5
    # )
]

### WIDGETS ###

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#b0b6b6",
                    background=["#5b6464", "#c3b4a0"],
                    borderwidth=2,
                    font='roman',
                    fontsize=12,
                    inactive="#3a4445",
                    this_current_screen_border="#a1a5a8"
                ),
                widget.Prompt(
                    prompt=prompt,
                    font='roman',
                    background=["#5b6464", "#c3b4a0"]
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=["#5b6464", "#c3b4a0"]
                ),
                widget.BatteryIcon(
                    background=["#5b6464", "#c3b4a0"]
                ),
                widget.Battery(
                    format='{percent:2.0%}',
                    background=["#5b6464", "#c3b4a0"],
                    foreground="#3a4445"
                ),
                widget.Sep(
                    background=["#5b6464", "#c3b4a0"],
                    linewidth=0,
                    padding=6
                ),
                widget.TextBox(
                    text="Vol:",
                    background=["#5b6464", "#c3b4a0"],
                    foreground="#3a4445"
                ),
                widget.Volume(
                    background=["#5b6464", "#c3b4a0"],
                    foreground="#3a4445"
                ),
                widget.Sep(
                    background=["#5b6464", "#c3b4a0"],
                    linewidth=0,
                    padding=6
                ),
                widget.Systray(
                    background=["#5b6464", "#c3b4a0"],
                    foreground="#3a4445"
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background=["#5b6464", "#c3b4a0"],
                    foreground="#3a4445"
                )
            ],
            24
        ),
        wallpaper="~/Downloads/walkway.jpg",
        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

lazy.cmd_spawn("picom")

