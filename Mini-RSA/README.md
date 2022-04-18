# Mini-RSA

## FLAG: picoCTF{e_sh0u1d_b3_lArg3r_60ef2420}

## Status: Complete

Category: Cryptography

Description: What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: ciphertext

> wget "https://mercury.picoctf.net/static/71f49c1459c00de5335d5dddc86c8841/ciphertext"

Attempted Wiener's Attack using python: wiener-attack.py

Attempted to run the "N" value through a prime factorization calulator: <https://www.alpertron.com.ar/ECM.HTM> to break down into p & q

Since e is really small I attempted to get the eth root of the cipher text, but too large causing overflow of int -> float

## NEED HELP - CREDIT: Dvd848 <https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Mini_RSA.md>

`In RSA, M**3 mod n = c. This can also be written as M**3 = tn + c for some t. So, this means that M = iroot(tn+c, 3). We just need to find the right t.`

Ran decode.py
Found i = 3533
Message: picoCTF{e_sh0u1d_b3_lArg3r_60ef2420}
