#!/bin/env python3
from pwn import *

# PROOF OF CONCEPT FOR ONE-TIME PAD - START #

flag = "hello"
flag2 = 'kfool'
key = 3
enc_text = ""

for c in flag2:
    enc_num = ord(c) ^ key
    enc_char = chr(enc_num)
    enc_text += enc_char
print(enc_text)

# PROOF OF CONCEPT FOR ONE-TIME PAD - END #