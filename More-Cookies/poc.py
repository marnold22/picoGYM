#!/bin/env pyhton3
from base64 import b64decode
from base64 import b64encode

print(ord("a"))
print(chr(ord("a")))

a = b64encode(b'a')
print(a)
a_dec = b64decode(a)
print(a_dec)

a = "YQo="
raw = b64decode(a)
list1 = list(raw)
list1[0] = chr(ord(list1[0]))
raw = ''.join(list1)
print(raw)
print(list1)
