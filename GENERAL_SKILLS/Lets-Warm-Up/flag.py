#!/bin/env python3

text = "0x70"
flag = bytearray.fromhex(text[2:]).decode()
print(f"picoCTF{{{flag}}}")