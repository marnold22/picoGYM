# Crackme-py

## FLAG: picoCTF{1|\/|_4_p34|\|ut_502b984b}

## STATUS: Complete

Category: Reverse-Engineer

Description: crackme-py

> wget "https://mercury.picoctf.net/static/db4b9e7a2862c320aa6b40e3551406bd/crackme.py"

After reading through crackme.py - the choose_greatest() function is irrelevant to the problem

However, the code shows it uses ROT47 - so using:
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

we can decode the secret by using ROT47 - cyberchef or flag.py
