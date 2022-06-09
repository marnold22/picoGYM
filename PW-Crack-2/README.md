# PW-Crack-2

## FLAG: picoCTF{tr45h_51ng1ng_502ec42e}

## Status: Complete

Category: General-Skills

Description: Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## STEPS

1. > wget <https://artifacts.picoctf.net/c/18/level2.py>
2. > wget <https://artifacts.picoctf.net/c/18/level2.flag.txt.enc>
3. Examine the level2.py file
   1. In here we see `pw_check()`
   2. But this time the value it compares is `chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)`
   3. Lets run that in python to get the values
4. python
   1. pw = chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)
   2. print(pw)
   3. RESPONSE: 39ce
5. Run python file
   1. > python level2.py
   2. Enter password: 39ce
   3. RESPONSE: Welcome back... your flag, user: `picoCTF{tr45h_51ng1ng_502ec42e}`
