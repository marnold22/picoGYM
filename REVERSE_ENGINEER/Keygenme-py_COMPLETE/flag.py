#!/bin/env python3

import hashlib

username_trial = "SCHOFIELD"
bUsername_trial = b"SCHOFIELD"
key_part1 = "picoCTF{1n_7h3_|<3y_of_"
key_part2 = ""
key_part3 = "}"

characters = []
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[4])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[5])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[3])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[6])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[2])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[7])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[1])
characters.append(hashlib.sha256(bUsername_trial).hexdigest()[8])

key_part2 = ''.join(characters)

flag = key_part1 + key_part2 + key_part3
print(flag)