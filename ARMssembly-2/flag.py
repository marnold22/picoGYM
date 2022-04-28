#!/bin/env python3
# HELP FROM: xnomas @ <https://ctftime.org/writeup/26964>

assembly_value = 1748687564
assembly_value_multiplied = assembly_value * 3

result = int(hex(assembly_value_multiplied), 16) & 0xffffffff
print(f'{result:08x}')