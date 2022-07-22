# Credstuff

## FLAG: picoCTF{C7r1F_54V35_71M3}

## Status: Complete

Category: Cryptography

Description: We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? Download the leak here. The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

## STEPS

1. Download the "leak"
   1. wget <https://artifacts.picoctf.net/c/534/leak.tar>
2. Extract file contents from tar file
   1. tar -xf leak.tar
3. In the usernames.txt we see `cultiris` on line 378 so let's grab the password that is on line 378 in the passwords.txt
   1. UN: `cultiris`
   2. PW: `cvpbPGS{P7e1S_54I35_71Z3}`
4. Looking at the 1st charater `c` and the 5th character `P` I know that they should be flipped `(c -> p)` and `(P -> C)` for `picoCTF`. That being said it looks like ROT13 cipher.
5. Ran through cyberchef
   1. Got successful flag!