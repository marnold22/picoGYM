# Python-Wrangling

## FLAG: picoCTF{4p0110_1n_7h3_h0us3_192ee2db}

Category: general skills
Description: Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

Pythonscript File:
> wget "https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py"

Password File:
> wget "https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/pw.txt"

Flag File:
> wget "https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/flag.txt.en"

Steps:

1. Get password
   > cat pw.txt
2. Use pythonscript to decode flag
    > python3 ende.py -d flag.txt.en
    > password = 192ee2db192ee2db192ee2db192ee2db

## FLAG

> picoCTF{4p0110_1n_7h3_h0us3_192ee2db}