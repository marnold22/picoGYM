# Enhance

## FLAG: picoCTF{3nh4nc3d_d0a757bf}

## Status: Complete

Category: Forensics

Description: Download this image file and find the flag. Download image file

## STEPS

1. wget <https://artifacts.picoctf.net/c/138/drawing.flag.svg>
2. Examining the drwing.flag.svg file we see inbetween each set of <tspan/> tags a letter
3. Breaking this apart we see:
   1. `p i c o C T F { 3 n h 4 n c 3 d _ d 0 a 7 5 7 b f }`
4. Removing the spaces we get:
   1. `picoCTF{3nh4nc3d_d0a757bf}`
