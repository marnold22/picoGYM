#!/usr/bin/env python3
import string

alphabet = string.ascii_uppercase

print(alphabet)

enc_flag = ['U','F','J','K','X','Q','Z','Q','U','N','B']
key = ['S','O','L','V','E','C','R','Y','P','T','O']
diff = []

diff.append((ord(enc_flag[0]) - ord(key[0]))%26)
diff.append((ord(enc_flag[1]) - ord(key[1]))%26)
diff.append((ord(enc_flag[2]) - ord(key[2]))%26)
diff.append((ord(enc_flag[3]) - ord(key[3]))%26)
diff.append((ord(enc_flag[4]) - ord(key[4]))%26)
diff.append((ord(enc_flag[5]) - ord(key[5]))%26)
diff.append((ord(enc_flag[6]) - ord(key[6]))%26)
diff.append((ord(enc_flag[7]) - ord(key[7]))%26)
diff.append((ord(enc_flag[8]) - ord(key[8]))%26)
diff.append((ord(enc_flag[9]) - ord(key[9]))%26)
diff.append((ord(enc_flag[10]) - ord(key[10]))%26)

print(diff)

flag = []
for val in diff:
    flag.append(alphabet[val])

print("".join(flag))
