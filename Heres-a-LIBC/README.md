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
