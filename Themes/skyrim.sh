# Script that changes laptop to the Skyrim theme

# Qtile
sed -i "s/colorschemes\..*/colorschemes\.skyrim import */" $HOME/.config/qtile/bars.py
sed -i "s/theme = \".*\"/theme = \"skyrim\"/" $HOME/.config/qtile/bars.py

# Alacritty
sed -i "s/colorschemes\/[^\.]*/colorschemes\/skyrim/" $HOME/.config/alacritty/alacritty.yml

# Bash Prompt
sed -i "s/theme=\".*\"/theme=\"skyrim\"/" $HOME/.bashrc

# Neovim
sed -i "s/colorscheme .*/colorscheme afterglow/" $HOME/.config/nvim/init.vim
sed -i "s/_theme = '.*'/_theme = 'zenburn'/" $HOME/.config/nvim/init.vim

# VS Code
sed -i "s/colorTheme\": \".*\"/colorTheme\": \"Ayu Dark\"/" $HOME/.config/Code\ -\ OSS/User/settings.json

# Spotify
sed -i "s/current_theme[^=]*=.*/current_theme {11}= burntSienna/" $HOME/.config/spicetify/config.ini
spicetify update

# Neofetch
sed -i "s/image_source=\"\$HOME\/\.config\/neofetch\/[^_]*/image_source=\"\$HOME\/\.config\/neofetch\/skyrim/" $HOME/.config/neofetch/config.conf

# Firefox (?)
# Slack (?)