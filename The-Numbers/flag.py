#!/bin/env python3

import string

the_numbers = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
flag = []

for num in the_numbers:
    flag.append(string.ascii_uppercase[num-1])
    
print("".join(flag))
