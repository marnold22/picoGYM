# New-Caesar

## FLAG: picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}

## Status: Complete

Category: Cryptography

Description: We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih new_caesar.py

> wget "https://mercury.picoctf.net/static/2fc43dd1a3718df7debf367b0e092831/new_caesar.py"


In the code we see:
`ALPHABET = string.ascii_lowercase[:16]` which tells us they only use the first 16 letters of the alphabet thus this particular Caesar Cipher is using base-16 encoding.

## Encode function pseudocode
 - convert the ascii value into binary
 - Take first 4 bits (of binary) and convert that value to string
 - Take last 4 bits (of binary) and convert that value to string
 - append all values into one string that is then passed to the shift() function

After encoding into base16 they then use the caesar or shift encoding method for the message.

To reverse this we must unshift first, then decode from base16

After running decode.py we get two possible outputs:
1. key = j : TcNcd.N/&(&U #"T!SP(SS"T&$$$S&"&!TT QQT
2. key = k : et_tu?_0797f143e2da9dd3e7555d7372ee1bbe

Knowing this is a Caesar Cipher `et_tu` seems appropriate so we will try that flag