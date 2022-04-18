# Cache-Me-Outside

## FLAG: picoCTF{97c85bbf2168f674263a1c5629b411a3}

## Status: Complete

Category: Binary-Exploit

Description: While being super relevant with my meme references, I wrote a program to see how much you understand heap allocations. nc mercury.picoctf.net 10097 heapedit Makefile libc.so.6

> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/heapedit"
> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/Makefile"
> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/libc.so.6"

## NOTES

- Makefile compiles the code and removes (rm) the heapedit file
- Glib tcache research <https://guyinatuxedo.github.io/29-tcache/tcache_explanation/index.html>

Tried running heapedit but here is the error
> ./heapedit
`[1]    713 segmentation fault  ./heapedit`

## NEED HELP - CREDIT Dvd848 <https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Cache_Me_Outside.md> & CREDIT <https://papadoxie.github.io/Writeups/PicoCTF/CacheMeOutside/CacheMeOutside.html>

## STEPS

1. Runing heapedit
    > ./heapedit
    ERROR: `[1]    713 segmentation fault  ./heapedit`

2. Run GDB on heapedit:
    > gdb ./heapedit

3. Check linker lib version & compare to system's version
    > strings libc.so.6 | grep version
    `GNU C Library (Ubuntu GLIBC 2.27-3ubuntu1.2) stable release version 2.27`
    > strings /usr/lib/x86_64-linux-gnu/libc-2.33.so | grep version
    `GNU C Library (Debian GLIBC 2.33-6) release release version 2.33`
    Our system is using a newer library

4. Run pwninit
    > pwninit
    > ./heapedit_patched
    `[1]    9883 segmentation fault  ./heapedit_patched`

5. Get decompiled code (decomp.c)

6. Edit the solve.py template with our variables

7. Run solve.py
    > python3 solve.py
    FLAG OUTPUT: picoCTF{97c85bbf2168f674263a1c5629b411a3}
