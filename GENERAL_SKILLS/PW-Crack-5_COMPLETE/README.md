# PW-Crack-5

## FLAG: picoCTF{h45h_sl1ng1ng_40f26f81}

## Status: Complete

Category: General-Skills

Description: Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

## STEPS

1. > wget <https://artifacts.picoctf.net/c/80/level5.py>
2. > wget <https://artifacts.picoctf.net/c/80/level5.flag.txt.enc>
3. > wget <https://artifacts.picoctf.net/c/80/level5.hash.bin>
4. > wget <https://artifacts.picoctf.net/c/80/dictionary.txt>
5. Python Script
   1. created test.py
      1. This reads in the dictionary file, strips it, and appends to a list
   2. Use this code in the level5.py
      1. Add a loop in the `level_5_pw_check()`

        ```py
        def level_5_pw_check():
            #user_pw = input("Please enter correct password for flag: ")
            for i in pw_input:
                print(f'Trying Password: {i}')
                user_pw_hash = hash_pw(i)
                ...
        ```

6. Run the level5.py
   1. OUTPUT: `Trying Password: 7e5f     picoCTF{h45h_sl1ng1ng_40f26f81}`
