# Pixelated

## FLAG: picoCTF{2a4d45c7}

## Status: Complete

Category: Cryptography

Description: I have these 2 images, can you make a flag out of them? scrambled1.png scrambled2.png

## STEPS

1. > wget <https://mercury.picoctf.net/static/49743139fb7c10765dbf462d40987d2a/scrambled1.png>
2. > wget <https://mercury.picoctf.net/static/49743139fb7c10765dbf462d40987d2a/scrambled2.png>
3. Run stegsolve
   1. Open `scrambled1.png` as image 1
   2. Analysis -> Image Combine
   3. Select `scrambled2.png` as second image
   4. Tab over to `ADD` section and we can see the flag
4. FLAG: `picoCTF{2a4d45c7}`
5. Save the image as `solved.bmp`
