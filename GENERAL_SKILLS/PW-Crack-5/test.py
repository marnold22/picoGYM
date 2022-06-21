#!/usr/bin/env python3
pw_input = []
pw_dict = open('dictionary.txt', 'r')
count = 0

for line in pw_dict:
    count +=1
    pw_input.append(line.strip())
pw_dict.close()

for i in pw_input:
    print(i)