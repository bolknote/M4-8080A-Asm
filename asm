#!/bin/bash

if [[ ! -f "$1" || -z "$1" ]]; then
    echo "Usage: $0 <in-file> <out-file>"
    exit 1
fi

if [[ -z "$2" ]]; then
	postproc() { grep -v '^ *$'; }
else
	filename="$2"	
	if [[ "$filename" == "/dev/stdout" || "$filename" == "-" ]]; then
		postproc() { xxd -r -p | hexdump -C; }
	else
		postproc() { xxd -r -p > "$filename"; }
	fi
fi

m4 asm8080.m4 <(m4 linker8080.m4 "$1") "$1" | postproc
