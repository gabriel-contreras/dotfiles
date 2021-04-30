## Configuration file for the Qtile WM
import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keys import keys
from screens import screens

mod = "mod4"

### GROUPS ###
group_names = [
    "WWW",
    "CODE",
    "QNTM",
    "NOTES",
    "DOC",
    "CHAT",
    "MUS",
    "ZOOM"
]
groups = [Group(name) for name in group_names]
for i, (name) in enumerate(group_names):
    keys.extend([
        Key([mod], str(i+1), lazy.group[name].toscreen()),
        Key([mod, "shift"], str(i+1), lazy.window.toGroup(name))
    ])

layouts = [
    layout.MonadTall(
        border_focus="#5b6464",
        border_width=4,
        margin=10,
        single_margin=14
    )
]

widget_defaults = dict(font='sans', fontsize=14, padding=5)

# Set the wallpaper
def wallpaper():
    path = '~/Downloads/skyrim.jpg'
    os.system('feh --bg-scale ' + path)

@hook.subscribe.startup
def autostart():
    wallpaper()

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "qtile"

@hook.subscribe.startup
def opacity():
    home = os.path.expanduser('/.config/qtile/autostart.sh')
    subprocess.call([home])