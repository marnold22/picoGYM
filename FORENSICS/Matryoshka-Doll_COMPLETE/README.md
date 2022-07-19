# Matryoshka-Doll

## FLAG: picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}

## STATUS: Complete

Category: Forensics

Description: Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this

Hint-1: Wait, you can hide files inside files? But how do you find them?
Hint-2: Make sure to submit the flag as picoCTF{XXXXX}

> wget "https://mercury.picoctf.net/static/2978e1270538613cd8181c7b0dabe9bd/dolls.jpg"
> file dolls.jpg
> strings dolls.jpg > strings.txt
> xxd dolls.jpg > hexdump-dolls
> binwalk dolls.jpg

output of binwalk:

DECIMAL       HEXADECIMAL     DESCRIPTION

--------------------------------------------------------------------------------

0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22

> binwalk --dd='.*' dolls.jpg

This extracts all data from the image

> file 0
Output: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
> file 4286C
Output: Zip archive data, at least v2.0 to extract, compression method=deflate
> file 9F150
Output: Zip archive data (empty)
> file C9A
Output: TIFF image data, big-endian, direntries=4, xresolution=62, yresolution=70, resolutionunit=2
> unzip 4286C
Just an image

### SOLUTION

After looking around at file structure you need to binwalk -e each of the nested folders starting with 2_c.jpg, then 3_c.jpg, 4_c.jpg inside here is the flag.txt
