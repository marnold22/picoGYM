#!/usr/bin/env python3

import string

alphabet = string.ascii_lowercase
cipher_text = 'ynkooejcpdanqxeykjrbdofgkq'
flag = []

offset = 97

while offset > 0:
    for letter in cipher_text:
        val = (ord(letter) - offset ) % 26
        flag.append(alphabet[val])
    flag.append("\n")
    offset = offset - 1

# Print out potential solutions and go through by hand
print("".join(flag))
