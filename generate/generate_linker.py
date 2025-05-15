#!/usr/bin/env python3

import re, os

script_dir = os.path.dirname(os.path.abspath(__file__))


print("""changequote([, ])dnl
define([__ip], 0)dnl
define([ORG], [])dnl])dnl
define([__pr], [define([__ip], eval(__ip + ifelse($2, [], 1, $2)))$1])dnl
define([__hex], [format([%02X %02X], eval($1 % 256), eval($1 >> 8))])dnl
define([__plusip], [[[__hex(eval($1 + __ip))]]])
define([LABEL], [define[]($1, __plusip(__ip))])dnl
define([ADDR], [])dnl
define([BYTE], [__pr([], $#)])""")

stats = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'H': [], 'L': [], 'M': [], 'SP': [], 'PSW': []}

names = set()

with open(script_dir + '/8080a.txt') as f:
		for line in f:
			name = line.strip().split(';')[0]
			
			if ' ' in name:
				(name, *args) = re.split('[ ,]+', name)
				if 'pp' in args or 'd8' in args:
					length = 2
				elif 'd16' in args or 'a16' in args:
					length = 3
				else:
					length = 1
			else:
				length = 1

			if name not in names:
				print(f'define([{name}], [__pr([], {length})])dnl')
				names.add(name)

for name in stats:
	print(f'define([{name}], [])dnl')

for x in range(0, 65535):
	print(f'define([H{x:X}], [])dnl')
