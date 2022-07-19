# Basic-mod2

## FLAG: picoCTF{1NV3R53LY_H4RD_8A05D939}

## Status: Complete

Category: Cryptography

Description: A new modular challenge!
Download the message here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## STEPS

1. wget <https://artifacts.picoctf.net/c/501/message.txt>
2. Create script to decode (similar to Basic-Mod1)
3. Run script to decode and get flag