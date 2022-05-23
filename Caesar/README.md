# Caesar

## FLAG: picoCTF{crossingtherubiconvfhsjkou}

## Status: Complete

Category: Cryptography

Description: Decrypt this message: <https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext>

## STEPS

1. > wget <https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext>
2. Python Script
   1. Get our cipher text
   2. Create lowercase alphabet
   3. Create an offset counter
   4. Iterate through ciphertext getting the ord() value
   5. Using this value as the iterator of the lowercase alphabet
   6. Loop through and get all possible values of the ciphertext decoded using first offset value
   7. Loop through all offset values to get ALL possible combinations of ciphertext decryptions
   8. Print out all potential solutions
3. After running the script I see only one that looks legible: `crossingtherubiconvfhsjkou`
4. flag = `picoCTF{crossingtherubiconvfhsjkou}`
