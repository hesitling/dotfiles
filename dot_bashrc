#!/bin/bash

[[ "${-}" != *i* ]] && return

# $1: name; $2: file
load_conf() {
    if [[ -f "${2}" ]]; then
        . "${2}"
    else
        printf '\033[01;31mWARN\033[00m:%s not found.\n' "${1}" 1>&2
    fi
}

HISTCONTROL=ignoreboth
HISTFILE="${HOME}/.histfile"
HISTSIZE=1024
HISTFILESIZE=8192

shopt -s autocd \
    cdspell \
    checkwinsize \
    complete_fullquote \
    expand_aliases \
    extglob \
    extquote \
    histappend \
    histverify \
    interactive_comments \
    no_empty_cmd_completion \
    progcomp \
    progcomp_alias

PS1='\[\033[01;32m\][$?]\[\033[01;35m\][\W]\n\[\033[01;36m\]\$\[\033[00m\] '
PS2='\[\033[01;32m\]+\[\033[00m\] '
printf -v PS3 '\033[01;32m>\033[00m '
PS4='\[\033[01;31m\]!\[\033[00m\] '

load_conf '~/.shrc' ~/.shrc
load_conf 'bash_completion' '/usr/share/bash-completion/bash_completion'

set +H -o emacs

export GPG_TTY="$(tty)"

if [[ ! -f ~/TODO.md ]]; then
echo 'TODO.md not exists! Do you remember what you should do?'
else
head --lines=-2 ~/TODO.md
echo 'Please check and add what you want to do in TODO.md'
fi
