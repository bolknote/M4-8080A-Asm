#!/bin/bash

if [[ ! -f "$1" || -z "$1" || -z "$2" ]]; then
    echo "Usage: $0 <in-file> <out-file>"
    exit 1
fi

m4 asm8080.m4 <(m4 linker8080.m4 "$1") "$1" | xxd -r -p > "$2"
