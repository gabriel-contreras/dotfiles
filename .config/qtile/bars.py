from libqtile import bar, widget

# Set the theme
from colorschemes.skyrim import *
theme = "skyrim"

if (theme == "skyrim"): prompt = "🍮: "

main_bar = bar.Bar(
    [
        widget.GroupBox(
            active= white,
            background = [grad1, grad2],
            borderwidth=2,
            fontsize=18,
            inactive = black,
            this_current_screen_border = current_group_border
        ),
        widget.Prompt(
            prompt=prompt,
            font='roman',
            background = [grad1, grad2]
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background = [grad1, grad2]
        ),
        widget.BatteryIcon(
            background = [grad1, grad2]
        ),
        widget.Battery(
            format='{percent:2.0%}',
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Sep(
            background = [grad1, grad2],
            linewidth=0,
            padding=6
        ),
        widget.TextBox(
            text="Vol:",
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Volume(
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Sep(
            background = [grad1, grad2],
            linewidth=0,
            padding=6
        ),
        widget.Systray(
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Clock(
            format='%Y-%m-%d %a %I:%M %p',
            background = [grad1, grad2],
            foreground=black
        )
    ],
    24
)
