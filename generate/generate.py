#!/usr/bin/env python3

import re, os

script_dir = os.path.dirname(os.path.abspath(__file__))

print("""changequote([, ])dnl
define([__hexdec], [
  eval(
    ifelse(len($1),2,
      [0x]substr($1,0,2),
      ifelse(len($1),4,
        [0x]substr($1,2,2)*256 + [0x]substr($1,0,2),
        []
      )
    )
  )
])dnl
define([__ip], 0)dnl
define([ORG], [define([__ip], [__hexdec($1)])dnl])dnl
define([__pr], [$1])dnl
define([__hex], [format([%02X %02X], eval($1 % 256), eval($1 >> 8))])dnl
define([LABEL], [define($1, __hex([__ip])) dnl])dnl
define([ADDR], [$1])dnl
define([BYTE], [__pr([$*])])""")

cmds = set()
stats = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'H': [], 'L': [], 'M': [], 'SP': [], 'PSW': []}

with open(script_dir + '/8080a.txt') as f:
	for line in f:
		(name, code) = line.strip().split(';')
		code = code.lower()

		if ' ' in name:
			(name, *args) = re.split('[ ,]+', name)

			r = [x for x in args if x in stats]
			if r:
				if name not in cmds:
					print(f'define([{name}], [define([__cmd], [__s_{name}])])dnl')
					cmds.add(name)

				match len(r):
					case 1:
						stats[r[0]] += [f'[__s_{name}], [__pr([{code}])]']
					case 2:
						stats[r[0]] += [f'[__s_{name}], [define([__cmd], [__s_{name}_{r[0]}])]']
						stats[r[1]] += [f'[__s_{name}_{r[0]}], [__pr([{code}])]']
			else:
				print(f'define([{name}], [__pr([{code}])])dnl')
		else:
			print(f'define([{name}], [__pr([{code}])])dnl')

for key, values in stats.items():
	print(f'define([{key}], [\nifelse(')
	for line in sorted(set(values)):
		print(f'    defn([__cmd]), {line},')
	print('    [])')
	print('])dnl')

for x in range(0, 65535):
	print(f'define([h{x:X}], [{x.to_bytes(2 if x > 255 else 1, "little").hex()}])dnl')
print()
