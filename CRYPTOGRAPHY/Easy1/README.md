# Easy1

## FLAG: picoCTF{CRYPTOISFUN}

## Status: Complete

Category: Cryptography

Description: The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

Encrypted Flag: `UFJKXQZQUNB`
Key: `SOLVECRYPTO`

## Steps

1. Convert letters in ENC_FLAG & KEY to integers
2. Subtract the Key value from the ENC_FLAG value
3. Need to make sure those values are in the 26 letters of alphabet so modulus "%" 26 on the subtracted values
4. Convert the subtracted values back into characters using the normal alphabet as the mapping (ie. A = 1, B = 2, etc...)
5. This will get the flag
6. picoCTF{CRYPTOISFUN}