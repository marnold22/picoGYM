#!/usr/bin/env python3
import requests

url = 'http://mercury.picoctf.net:45028/'

post1 = requests.get(url)
post2 = requests.post(url)
post3 = requests.head(url)
post4 = requests.put(url)
post5 = requests.delete(url)

print(post1.headers)
print(post2.headers)
print(post3.headers)
print(post4.headers)
print(post5.headers)