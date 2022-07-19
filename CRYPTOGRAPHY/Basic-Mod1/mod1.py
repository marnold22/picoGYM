#!/usr/bin/env python3
import string

alphabet = string.ascii_uppercase + string.digits + '_'
enc_message = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397]
dec_message = []

# Create list of all values mod 37
mod_vals = []
for val in enc_message:
    dec = val % 37
    mod_vals.append(dec)

# Map each value to the corresponding alphabet position + number + '_'
for mod_val in mod_vals:
    dec_message.append(alphabet[mod_val])

print("picoCTF{"+"".join(dec_message)+"}")