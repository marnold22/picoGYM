# PW-Crack-3

## FLAG: picoCTF{m45h_fl1ng1ng_2b072a90}

## Status: Complete

Category: General-Skills

Description: Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## STEPS

1. > wget <https://artifacts.picoctf.net/c/23/level3.py>
2. > wget <https://artifacts.picoctf.net/c/23/level3.flag.txt.enc>
3. > wget <https://artifacts.picoctf.net/c/23/level3.hash.bin>
4. Opening the level3.py we see a comment that shows us the 7 possible passwords
   1. `pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]`
5. > python level3.py
   1. Password[0] -> That password is incorrect
   2. Password[1] -> That password is incorrect
   3. Password[2] -> That password is incorrect
   4. Password[3] -> `picoCTF{m45h_fl1ng1ng_2b072a90}`
   5. Password[4] -> That password is incorrect
   6. Password[5] -> That password is incorrect
   7. Password[6] -> That password is incorrect
