# Patchme_py

## FLAG: picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}

## Status: Complete

Category: Reverse-Engineer

Description: Can you get the flag?
Run this Python program in the same directory as this encrypted flag.

## STEPS

1. wget <https://artifacts.picoctf.net/c/388/patchme.flag.py> -> This is the python program
2. wget <https://artifacts.picoctf.net/c/388/flag.txt.enc> -> This is the encoded flag
3. Examine the patchme.py file
   1. In here we see the `level_1_pw_check()`
   2. Inside the function it checks for a password, and that passowrd is hardcoded
        ```py
            if( user_pw == "ak98" + \
                        "-=90" + \
                        "adfjhgj321" + \
                        "sleuth9000"):
        ```
    3. Concatenating all of these strings we get: `ak98-=90adfjhgj321sleuth9000`
4. Run the python script
5. Enter password
6. Get flag: `picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}`