# Always colorcode the ls command
alias ls='ls --color=auto'

# Alternative, cleaner version of ls for smaller directories
alias lt='ls --human-readable --size -1 -S --classify'

# List of all the mounted filesystems on the computer
alias mnt="mount | awk -F' ' '{ printf \"%s\t%s\n\",\$1,\$3; }' | column -t | egrep ^/dev/ | sort"

# Git Status
alias gs="git status"

# Git commit and add
alias gac="git commit -am"

# Git clone
alias gc="git clone"

# Edit the awesome config
alias cfg-awesome="cd $HOME/.config/awesome/ && nvim rc.lua"

# Edit the qtile config
alias cfg-qtile="cd $HOME/.config/qtile/ && nvim config.py"

# Edit the nvim config
alias cfg-nvim="cd $HOME/.config/nvim/ && nvim init.vim"

# Edit the Kitty Terminal config
alias cfg-kitty="cd $HOME/.config/kitty/ && nvim kitty.conf"

# Edit the Alacritty Terminal config
alias cfg-ala="cd $HOME/.config/alacritty/ && nvim alacritty.yml"
