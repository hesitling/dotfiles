#!/bin/zsh

[[ "${-}" != *i* ]] && return

# $1: name; $2: file
load_conf() {
    if [[ -f "${2}" ]]; then
        . "${2}"
    else
        printf '\033[01;31mWARN\033[00m:%s not found.\n' "${1}" 1>&2
    fi
}

HISTFILE="${HOME}/.histfile"
HISTSIZE=1024
SAVEHIST=8192

setopt autocd beep extendedglob noautoremoveslash nomatch
unsetopt notify

# Use `showkey -a` to get keycode
bindkey -e
bindkey -- "${terminfo[khome]}"   beginning-of-line
bindkey -- "${terminfo[kend]}"    end-of-line
bindkey -- "${terminfo[kich1]}"   overwrite-mode
bindkey -- "${terminfo[kbs]}"     backward-delete-char
bindkey -- "${terminfo[kdch1]}"   delete-char
bindkey -- "${terminfo[kcuu1]}"   up-line-or-history
bindkey -- "${terminfo[kcud1]}"   down-line-or-history
bindkey -- "${terminfo[kcub1]}"   backward-char
bindkey -- "${terminfo[kcuf1]}"   forward-char
bindkey -- "${terminfo[kpp]}"     beginning-of-buffer-or-history # <C-PageUp>
bindkey -- "${terminfo[knp]}"     end-of-buffer-or-history # <C-PageDown>

PS1='%B%(?.%F{green}.%F{red})[%?]%f%F{magenta}[%1~]%f'$'\n''%F{cyan}%#%f%b '
PS2='%B%F{green}+%f%b '
PS3='%B%F{green}>%f%b '
PS4='%B%F{red}!%f%b '

load_conf '~/.shrc' ~/.shrc
load_conf 'zsh-autosuggestions' '/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh'
load_conf 'zsh-syntax-highlighting' '/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh'

zstyle ':completion:*' menu select=0 search
zstyle ':completion:*' verbose yes
autoload -Uz compinit
compinit

export GPG_TTY="$(tty)"
