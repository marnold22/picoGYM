#!/usr/bin/env python3
import requests

url = 'http://mercury.picoctf.net:36622'

headers = {
    # Step 1
    "User-Agent":"PicoBrowser",

    # Step 2
    "Referer":"http://mercury.picoctf.net:36622",

    # Step 3
    "Date":"Tue, 22 May 2018 08:12:31 GMT",

    # Step 4
    "DNT":"0",

    # Step 5
    "X-Forwarded-For":"1.208.104.169",

    # Step 6
    "Accept-Language":"sv"
}

response = requests.get(url, headers=headers)
print(response.json())