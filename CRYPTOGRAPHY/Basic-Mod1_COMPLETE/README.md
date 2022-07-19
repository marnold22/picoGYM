# Basic-Mod1

## FLAG: picoCTF{R0UND_N_R0UND_B6B25531}

## Status: Complete

Category: Cryptography

Description: We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## STEPS

1. > wget <https://artifacts.picoctf.net/c/394/message.txt>
2. Create python script to perform mod
3. Run python script to decode message
