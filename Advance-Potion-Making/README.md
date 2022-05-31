# Advance-Potion-Making

## FLAG: picoCTF{w1z4rdry}

## Status: Complete

Category: Forensics

Description: Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

## STEPS

1. > wget <https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making>
2. > file advance-potion-making
   1. RESPONSE: data
3. We see that the file is quite large and strings didn't show anythiong so lets try binwalk
4. > Binwalk advance-potion-making
   1. RESPONSE: Zlib compressed data, compressed
   2. Let's extract it
   3. > binwalk -e advance-potion-making
   4. get a .zlib file

5. After racking my brain on .zlib and making no progress I sought out help which showed I was definitely on the **WRONG** path!!!

## NEED HELP CREDIT: ret2basic

1. Need to open original file in hexeditor
2. Change the following...
   1. 89 50 42 11  0D 0A 1A 0A   00 12 13 14  49 48 44 52
3. To the correct PNG file format
   1. 89 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52
   2. Changed the 42 11 -> 4E 47 and 00 12 13 14 -> 00 00 00 0D
4. Now lets try and open the image with eog
   1. No luck, just bright red
5. Lets open with stegsolve
   1. `picoCTF{w1z4rdry}`
