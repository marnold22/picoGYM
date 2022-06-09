#!/usr/bin/env python3
from collections import Counter
from string import ascii_lowercase

with open('public/study-guide.txt', 'r') as f:
    ciphertext = f.read()

charcount = Counter(c for c in ciphertext if c in ascii_lowercase)
total_chars = sum(charcount.values())
for char, count in charcount.items():
    print(f"{char}: {(count*100)/total_chars}% ({count})")
