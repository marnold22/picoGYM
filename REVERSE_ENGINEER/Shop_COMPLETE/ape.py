#!/bin/env python3

chars = [112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 109, 101, 114, 95, 53, 57, 49, 97, 56, 57, 53, 97, 125]
flag = []
for char in chars:
    flag.append(chr(char))

print("".join(flag))