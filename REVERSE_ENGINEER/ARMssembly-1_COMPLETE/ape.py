#!/bin/env python3

# START NOTES #

# STEP 0
# Load user input
user_input = 77

# STEP 1
# Left Bit Shift
# lsl w0, w1, w0 which means take w1 and shift it by w0 to the left
w0 = 2
w1 = 58
lsl = w1 << w0
print(lsl)

# STEP 2
# sdiv w0, w1, w0 which means take w1 and divide // by w0
w1 = 232
w0 = 3
sdiv = w1 // w0
print(sdiv)

# STEP 3
# sub w0, w1, w0 which means take w1 and subtract w0 (w1 - w0)
w1 = 77
w0 = user_input
sub = w1 - w0
print(sub)

# CONVERT TO HEX AND MAKE 32 BITS (remove '0b' prefix)
# Have to add zfill of 8 to make sure the value is 8 characters long (ie. 32 bit)
flag = hex(user_input)
print(flag[2:].zfill(8))
