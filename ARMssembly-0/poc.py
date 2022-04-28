#!/bin/env python3
# FROM THE DESCRIPTION:
# picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
# This is a poc that converts the 5614267 -> 0055aabb

def intTOhex(num):
    flag = '0x{0:08X}'.format(num)
    return "picoCTF{" + str(flag.lower()[2:]) + "}"

test = 5614267
print(intTOhex(test))

w0 = 3854998744
print(intTOhex(w0))


