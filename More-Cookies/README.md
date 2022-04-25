# More-Cookies

## FLAG: picoCTF{cO0ki3s_yum_2d20020d}

## Status: Complete

Category: Web-Exploit

Description: I forgot Cookies can Be modified Client-side, so now I decided to encrypt them! <http://mercury.picoctf.net:21553/>
HINTS 1: <https://en.wikipedia.org/wiki/Homomorphic_encryption>
HINTS 2: The search endpoint is only helpful for telling you if you are admin or not, you won't be able to guess the flag name

Homomorphic-Encryption: Homomorphic encryption is a form of encryption that permits users to perform computations on its encrypted data without first decrypting it. These resulting computations are left in an encrypted form which, when decrypted, result in an identical output to that produced had the operations been performed on the unencrypted data

> wget "http://mercury.picoctf.net:21553/"

Tried encoding and decoding several cookies using base64 with variations like:
admin
admintrue
admin1

## NEED HELP - CREDIT abbas <https://ctftime.org/writeup/27021>

This particular challenge uses a cbc bitflip

Ran flag.py and set range to 50
