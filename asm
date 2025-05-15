#!/bin/bash

if [[ ! -f "$1" || -z "$1" ]]; then
    echo "Usage: $0 <in-file> <out-file>"
    exit 1
fi

if [[ -z "$2" ]]; then
	m4 asm8080.m4 <(m4 linker8080.m4 "$1") "$1" | grep -v '^ *$'
else
	m4 asm8080.m4 <(m4 linker8080.m4 "$1") "$1" | xxd -r -p > "$2"
fi
