# Unsubscriptions-Are-Free

## FLAG: picoCTF{d0ubl3_j30p4rdy_ad77070e}

## Status: Complete

Category: Binary-Exploit

Description: Check out my new video-game and spaghetti-eating streaming channel on Twixer! program and get a flag. source nc mercury.picoctf.net 6312

## STEPS

1. > wget <https://mercury.picoctf.net/static/707147dc7d4abcec44d6ec17c32c701e/vuln>
2. > wget <https://mercury.picoctf.net/static/707147dc7d4abcec44d6ec17c32c701e/vuln.c>
3. > file vuln
   1. ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=89699d062dc4f47448ba7c5c03105267c060ce30, not stripped
4. > file vuln.c
   1. C source, ASCII text
5. Create an exploit.py file
6. Examine the Source code (vuln.c)
   1. In here we see a `hahaexploitgobrrr()` function that is essentailly our win function
   2. the win() function is called from `void s()`
   3. To access s() we need to reach `case 'S':` in the switch statement whihc requires a user to be authenticated
7. When running the vuln binary and choosing case S we get the following response: `OOP! Memory leak...0x80487d6`
8. However in that original menu we see that we can call i() multiple times which frees our user pointer

## NEED HELP CREDIT: papadoxie <https://papadoxie.github.io/Writeups/PicoCTF/UnsubscriptionsAreFree/UnsubscriptionsAreFree.html>

This write up explained vuln and the python script used to get the flag
