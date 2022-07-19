#!/bin/env python3
# CREDIT - Dvd848 https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Easy_Peasy.md

# I rewrote David's script to condense it that way I understood what each line was doing and how it was manipulating the key/flag bytes

from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000

r = remote("mercury.picoctf.net", 41934)
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}")
bin_flag = unhex(flag)

buffer = KEY_LEN - len(bin_flag)

print("THIS IS THE COUNTER: ", buffer)
print("THIS IS THE BIN_FLAG: ", bin_flag)

with log.progress('Causing wrap-around') as p:
    r.sendlineafter("What data would you like to encrypt? ", "a" * buffer)
    r.sendlineafter("What data would you like to encrypt? ", bin_flag)
    r.recvlineS()
    log.success("The flag: {}".format(unhex(r.recvlineS())))