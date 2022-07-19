# Strings-It

## FLAG: picoCTF{5tRIng5_1T_d66c7bb7}

## Status: Complete

Category: General-Skills

Description: Can you find the flag in file without running it?

## STEPS

1. > wget "https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings"
2. > strings -n 10 > strings-10.txt
   1. This grabs all srings (longer than 10 characters) and outputs to text file
3. > grep "picoCTF" strings-10.txt
   1. This searches the text file for a string containing `picoCTF`
4. Output: `picoCTF{5tRIng5_1T_d66c7bb7}`
