#!/usr/bin/env python3
import string

alphabet = string.ascii_uppercase + string.digits + '_'
enc_message = [104, 290, 356, 313, 262, 337, 354, 229, 146, 297, 118, 373, 221, 359, 338, 321, 288, 79, 214, 277, 131, 190, 377]
dec_message = []

# Create list of Modular Inverse Values using the value 41 as the modulus
# In python we can use the pow() function with -1 to find the modular inverse
mod_vals = []
for val in enc_message:
    dec = pow(val, -1, 41)
    mod_vals.append(dec)

# Map each inverse_mod value to the corresponding alphabet position + number + '_'
# In this mapping we need to subtract 1 from the alphabet index as the mod_vals are from 1-26 instead of 0-25
for mod_val in mod_vals:
    dec_message.append(alphabet[mod_val-1])

print("picoCTF{"+"".join(dec_message)+"}")