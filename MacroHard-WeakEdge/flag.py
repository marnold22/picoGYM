#!/bin/env python3

import base64

hidden = "ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ"
flag = base64.decode(hidden)
print(flag)