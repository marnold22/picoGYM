
from binascii import unhexlify

hexvals = [
    '6f636970',
    '7b465443',
    '306c5f49',
    '345f7435',
    '6d5f6c6c',
    '306d5f79',
    '5f79336e',
    '32666331',
    '30613130',
    'ff9a007d',
    'f7f38af8',
    'f7f0b440',
    '2753b500'
]

flag_b = []

for hex in hexvals:
    nexthex = unhexlify(hex)[::-1]
    nexthex = nexthex.strip()
    flag_b.append(nexthex)
print(b''.join(flag_b))
