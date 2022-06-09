# Glitch-Cat

## FLAG: picoCTF{gl17ch_m3_n07_bda68f75}

## Status: Complete

Category: General-Skills

Description: Our flag printing service has started glitching! nc saturn.picoctf.net 51109

## STEPS

1. > nc saturn.picoctf.net 51109
   1. RESPONSE: 'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
2. python
   1. flag = 'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
   2. print(flag)
   3. RESPONSE: `picoCTF{gl17ch_m3_n07_bda68f75}`
