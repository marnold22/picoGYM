# Some-Assembly-Required-1

## FLAG: picoCTF{a8bae10f4d9544110222c2d639dc6de6}

## Status: Complete

Category: Web-Exploit

Description: <http://mercury.picoctf.net:37669/index.html>

## STEPS

1. Navigate to website <http://mercury.picoctf.net:37669/index.html>
    - This is just an input form, so I checked the header for any static files and saw a js file
    - `G82XCw5CX3.js`

2. Pulled down the js file and beautified it so it was readable
    > wget <http://mercury.picoctf.net:37669/G82XCw5CX3.js>

3. Created a `deobfuscated.js` to manipulate and deobfuscate

4. Noticed a webassembly binary module
    > wget <http://mercury.picoctf.net:37669/JIFxzHyW8W>

5. Ran strings on the binary file
    - OUTPUT: picoCTF{a8bae10f4d9544110222c2d639dc6de6}
