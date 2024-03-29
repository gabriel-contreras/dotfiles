# Script that changes laptop to the Star Wars theme

# Qtile
sed -i "s/colorschemes\..*/colorschemes\.sw import */" $HOME/.config/qtile/bars.py
sed -i "s/theme = \".*\"/theme = \"sw\"/" $HOME/.config/qtile/bars.py

# Alacritty
sed -i "s/colorschemes\/[^\.]*/colorschemes\/sw/" $HOME/.config/alacritty/alacritty.yml

# Bash Prompt
sed -i "s/theme=\".*\"/theme=\"sw\"/" $HOME/.bashrc

# Neovim
sed -i "s/colorscheme .*/colorscheme parsec/" $HOME/.config/nvim/init.vim
sed -i "s/_theme = '.*'/_theme = 'distinguished'/" $HOME/.config/nvim/init.vim

# VS Code
sed -i "s/colorTheme\": \".*\"/colorTheme\": \"Kimbie Dark\"/" $HOME/.config/Code\ -\ OSS/User/settings.json

# Spotify
sed -i "s/current_theme[^=]*=.*/current_theme = noSleep/" $HOME/.config/spicetify/config.ini

# Neofetch
sed -i "s/image_source=\"\$HOME\/\.config\/neofetch\/[^_]*/image_source=\"\$HOME\/\.config\/neofetch\/sw/" $HOME/.config/neofetch/config.conf

# Firefox (?)
# Slack (?)

# Apply the changes
spicetify update
qtile cmd-obj -o cmd -f restart
