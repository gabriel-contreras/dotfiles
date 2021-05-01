from libqtile import bar, widget

# Set the theme
from colorschemes.skyrim import *
theme = "skyrim"

if (theme == "skyrim"): prompt = "🍮: "
elif (theme == "gow"): prompt = "𝝮: "

main_bar = bar.Bar(
    [
        widget.GroupBox(
            active= white,
            background = [grad1, grad2],
            borderwidth=3,
            margin_x = 10,
            fontsize=20,
            inactive = black,
            this_current_screen_border = current_group_border
        ),
        widget.Prompt(
            prompt=prompt,
            font='firacode',
            cursor_color = white,
            fontshadow = current_group_border,
            foreground = white,
            background = [grad1, grad2]
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background = [grad1, grad2]
        ),
        widget.Systray(
            font = 'firacode',
            background = [grad1, grad2],
            foreground=black
        ),
        widget.TextBox(
            text="",
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Battery(
            format='{percent:2.0%}',
            font = 'firacode',
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Sep(
            background = [grad1, grad2],
            linewidth=0,
            padding=6
        ),
        widget.TextBox(
            text="",
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Volume(
            font = 'firacode',
            background = [grad1, grad2],
            foreground=black
        ),
        widget.Sep(
            background = [grad1, grad2],
            linewidth=0,
            padding=6
        ),
        widget.TextBox(
            text = "",
            background = [grad1, grad2],
            foreground = black
        ),
        widget.Clock(
            format='%I:%M %p',
            font = 'firacode',
            background = [grad1, grad2],
            foreground=black
        )
    ],
    24
)
