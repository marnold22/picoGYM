enc = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

dec = rot47(enc)
print(dec)