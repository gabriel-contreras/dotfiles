from libqtile import bar, widget
import os
import socket

prompt = "🍮: "

main_bar = bar.Bar(
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
)