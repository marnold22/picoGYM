# Easy-peasy

## FLAG: picoCTF{abf2f7d5edf082028076bfd7a4cfe9a9}

## STATUS: Complete 

Category: Cryptography

Description: A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 41934 otp.py

> wget "https://mercury.picoctf.net/static/1f148e5cdf8bd2c9f752b14d46a3f2f2/otp.py"
> nc mercury.picoctf.net 41934
Response: This is the encrypted flag! 0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d

## Understanding the python code

Key-length is 50000 bytes (ie XOR pad of length 50000)
This is a one time pad, BUT because of the code portion:
`if stop >= KEY_LEN:`
`stop = stop % KEY_LEN`

## HELP - CREDIT - Dvd848 <https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Easy_Peasy.md>

We know that the service performs a wrap-around and reuses the same pad for every 50000 characters
