source /etc/profile

# PS1
export PS1="\[$(tput bold)\]\[\033[38;5;1m\][\[$(tput sgr0)\]\[\033[38;5;227m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;39m\]\h\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;39m\]\W\[$(tput sgr0)\]\[\033[38;5;1m\]]\[$(tput sgr0)\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"

# navigation
alias ..='cd ..' 
alias ...='cd ../..'

# broot
alias br='br -dhp'
alias bs='br --sizes'

# Doom Emacs
alias doom='~/.emacs.d/bin/doom'

alias ls='exa -al --color=always --group-directories-first' 
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'

