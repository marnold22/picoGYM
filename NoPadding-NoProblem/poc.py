#!/bin/env python3
import binascii

e = 65537
n = 30994968412821274638126108542140224647370292100079091608343041083209715023181825537637957453183815788151099869840363450721
d = 10949944362147351445695313961215384000802056441294706923101734114824865877971959648683318864984560110549528540371119079473

orig_message = 'My credit card number is 1337'
print(orig_message)

# Encode message string to hex
m = binascii.hexlify(b'My credit card number is 1337')
# Cast m as an integer from the returned bytes of hexlify
m = int(m, 16)
print(m)

# Compute ciphertext c=m^e mod n
ct = pow(m, e, n)
print(ct)

# Decode ciphertext to plain text p=c^d mod n  --- Note this will return the hex value so need to unhexlify
pt = pow(ct, d, n)
print(pt)
pt = hex(pt)
print(bytearray.fromhex(pt[2:]).decode())
