#!/bin/env python3
#!/bin/env python3

import string

offset = ord("a")
alphabet = string.ascii_lowercase[:16]

cipher = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

for i,c in enumerate(cipher):
    print(f'{i} {c}')

def unshift(c, k):
    t1 = ord(c) + offset
    t2 = ord(k) + offset
    return alphabet[(t1 + t2) % len(alphabet)]

def b16_decode(enc):
    for e in enc:
        p1 = f"{alphabet.index(enc[:1]):04b}"
        p2 = f"{alphabet.index(enc[1:]):04b}"

        binary = p1 + p2
        char = chr(int(binary,2))

        return char

def check(text):
    for t in text:
        if t not in string.printable:
            return False
    return True

for val in alphabet:
    plain = ''
    key = val
    decode = ''

    for i,c in enumerate(cipher):
        decode += unshift(c, key)

    for i in range(0, len(decode), 2):
        temp = (decode[i] + decode[i+1])

        plain += b16_decode(temp)

    if check(plain):
        print(f'key = {val} : {plain} ')
        print() 