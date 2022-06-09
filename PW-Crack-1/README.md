# PW-Crack-1

## FLAG: picoCTF{545h_r1ng1ng_fa343060}

## Status: Complete

Category: General-Skills

Description: Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## STEPS

1. > wget <https://artifacts.picoctf.net/c/52/level1.py>
2. > wget <https://artifacts.picoctf.net/c/52/level1.flag.txt.enc>
3. Examine level1.py
   1. In here we see a `pw_check()` which uses the value `1e1a`
4. Run level1.py
   1. > python level1.py
   2. "Please enter correct password for flag: `1e1a`"
   3. RESPONSE: Welcome back... your flag, user: `picoCTF{545h_r1ng1ng_fa343060}`
