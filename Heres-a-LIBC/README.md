# Heres-a-LIBC

## FLAG: picoCTF{}

## Status: Incomplete

Category: Binary-Exploit

Description: I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 62289

Hint-1: PWNTools has a lot of useful features for getting offsets.

> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/vuln"
> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/libc.so.6"
> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/Makefile"

## STEPS

1. Try running pwninit
    > pwninit
    > configure solve.py with addr: mercury.picoctf.net, 62289
    > python3 solve.py

2. Run ./vuln_patched
    > insert "AAAAAAA..." until segmentation error

3. Use Ghidra to decompile and analyze code
    > main() -> copied to decomp.c
    > doStuff() -> copied to decomp.c
        > doStuff() makes space for 112 characters but only "converts" 100 of those characters
    > puts() function is used in both main() and doStuff() which is exploitable

4. Used pwninit solve.py to send data
    > r.sendline(b'A' * 136)
      - 135 A's works but overflows at 136
    > r.sendline(b'A' x 112)
    **MAYBE USES ROP ATTACK?**

5. python3 POC
    > len("AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa")
    - returns 112
    > len("AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa")
    - returns 100

6. Need to craft a ROP chain
   1. Need to find the EIP (Extended Instruction Pointer)
   2. Run GNU debugger (gdb) and put breackpoint on main()
      > gdb ./vuln_patched
      > b main
      > pattern create 136
