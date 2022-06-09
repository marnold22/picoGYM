#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("mercury.picoctf.net", 62289)

    return r


def main():
    r = conn()

    # good luck pwning :)
    # r.sendline(b'A'*135) # 135 works, 136 causes overflow
    
    r.sendline(b'A' * 112)
    r.interactive()


if __name__ == "__main__":
    main()
