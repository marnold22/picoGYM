# Fixme2.py

## FLAG: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}

## Status: Complete

Category: General-Skills

Description: Fix the syntax error in the Python script to print the flag.

## STEPS

1. > wget <https://artifacts.picoctf.net/c/65/fixme2.py>
2. Python File
   1. On inspection we see `# Check that flag is not empty if flag = "":`
   2. We need to correct the check for empty
   3. `if flag == "":`
3. > python fixme2.py
   1. RESPONSE: That is correct! Here's your flag: `picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}`
