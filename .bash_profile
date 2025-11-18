#!/bin/bash

load_conf() {
    if [[ -f "${2}" ]]; then
        . "${2}"
    else
        printf '\033[01;31mWARN\033[00m:%s not found.\n' "${1}" 1>&2
    fi
}

load_conf '~/.shenv' ~/.shenv
load_conf '~/.bashrc' ~/.bashrc
