#!/bin/env python3

import string

##### - Personal Understanding - #####
# The offset is 97
offset = ord("a")

# The alphabet is the first 16 lowercase characters (ie. a - p)
alphabet = string.ascii_lowercase[:16]

# This converts the character value into its binary vale (all 8 digits)
binary = "{0:08b}".format(ord("a"))

# This encodes the first 4 bits and last 4 bits as two seperate characters
# The second parameter in int(param1, param2) "2" means convert to decimal
l1 = alphabet[int(binary[:4], 2)]
l2 = alphabet[int(binary[4:], 2)]

# After running these we can see that when using the letter "a" -> we get the encoded letters gb
print(binary)
print(l1, l2)

#  For the two variables we get two characters, and substract 97 from their ascii values. Then just add those together (modulo length of the alphabet so we stay in bounds) and use that value as an index for the alphabet list.
def shift(c, k):
	t1 = ord(c) - offset
	t2 = ord(k) - offset
	return alphabet[(t1 + t2) % len(alphabet)]

##### - Personal Understanding - #####

##### - LETS SOLVE - #####
# GO TO decode.py
