import subprocess

from libqtile.config import Key
from libqtile.command import lazy

BROWSER = "firefox"
TERM_EMULATOR = "alacritty"
MUSIC_PLAYER = "spotify"
FILE_MANAGER = "pcmanfm"
NOTES = "notion-app"

mod = "mod4"

# add 'PlayPause', 'Next', or 'Previous'
music_cmd = ('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
             '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.')

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Move windows between left/right columns or move up/down in current stack
    # Moving out of range in Columns layout will create new column
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Screen
    # Cheap/ugly way for brightness for now, fix this later!!)
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo light -U 10")),

    # Audio
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 2- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 2+ unmute")),
    Key([], "XF86AudioPlay", lazy.spawn(music_cmd + 'PlayPause')),
    Key([], "XF86AudioNext", lazy.spawn(music_cmd + 'Next')),
    Key([], "XF86AudioPrev", lazy.spawn(music_cmd + 'Previous')),

    # Apps
    Key([mod], "Return", lazy.spawn(TERM_EMULATOR)),
    Key([mod], "b", lazy.spawn(BROWSER)),
    Key([mod], "e", lazy.spawn(FILE_MANAGER)),
    Key([mod], "z", lazy.spawn("zoom")),
    Key([mod], "s", lazy.spawn("slack")),
    Key([mod], "n", lazy.spawn(NOTES)),
    Key([mod], "m", lazy.spawn(MUSIC_PLAYER)),

    # Screenshots
]