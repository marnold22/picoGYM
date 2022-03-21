#!/bin/env python3

# Original Code:
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Encoded TXT:
enc = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
enc_nums = []
flag = []

# Get ascii values for each encoded character
for i in range(len(enc)):
    enc_nums.append(ord(enc[i]))

# This gets half the flag
for num in enc_nums:
    flag.append(chr(num >> 8))
    
print(''.join(flag))

# Add rest to cyberchef