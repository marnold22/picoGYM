# Transformation

## FLAG: picoCTF{16_bits_inst34d_of_8_75d4898b}

Category: Reverse-Engineering

Description: I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

> wget "https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc"

## Decode.py

Ran decode.py that gets half the flag, then added enc to cyberchef with "magic" settings and "intensive mode" - scroll down

Encode_text('UTF-16BE (1201)') = picoCTF{16_bits_inst34d_of_8_75d4898b}
