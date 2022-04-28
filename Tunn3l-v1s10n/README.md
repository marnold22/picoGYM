# Tunn3l-v1s10n

## FLAG: picoCTF{qu1t3_a_v13w_2020}

## STATUS: Complete

Category: Forensics

Description: We found this file. Recover the flag.

Hint-1: Weird that it won't display right...

> wget "https://mercury.picoctf.net/static/01be2b38ba97802285a451b94505ea75/tunn3l_v1s10n"
> strings tunn3l_v1s10n > strings
> xxd tunn3l_v1s10n > hexdump-tunnel
> more tunn3l_v1s10n
> exiftool tunn3l_v1s10n > exiftool-report

## RESOURCES

<https://en.wikipedia.org/wiki/BMP_file_format>

In a BMP file the first 2 bytes (magic number or headerfield) are:
0x42 0x4D

The first 14 bytes are the BMP file header, the structure is as follows:
|header| + |size_of_bmp| + |reserved| + |reserved| + |offset_or_starting_addr|
|2 bytes| + |4 bytes| + |2 bytes| + |2 bytes| + |4 bytes|

The first 24 bytes of the `tunn3l_v1s10n` file are:
| 42 4D 8E 26 2C 00 00 00 00 00 BA D0 00 00 | BA D0 00 00 6E 04 00 00 32 01 |
| BMP-HEADER |

## HELP NEEDED - CREDIT GOES TO ZeroDayTea / Killer Queen from <https://ctftime.org/writeup/28157>

'Seeing as the number of bytes in the DIB header are wrong and the number of bits per pixel are also wrong we realize we need to edit the bytes at offset 0x0e and 0x1c. The correct bytes are as follows:'

| 42 4d 8e 26 2c 00 00 00 00 00 ba d0 00 00 28 00 00 00 6e 04 00 00 40 03 |

Changing the "ba d0" of the DIB header num-bytes to "28 00" and changing the "32 01" of the number of bits per pixel to "40 03" does the trick and we get the proper image. Renaming the "tunn3lv1s10n" file to "tunn3lv1s10n.bmp" we are able to open it and get the flag.

## COMPARISON

In comparison the original bytes to the new bytes are:
| 42 4D 8E 26 2C 00 00 00 00 00 BA D0 00 00 BA D0 00 00 6E 04 00 00 32 01 |
| 42 4d 8e 26 2c 00 00 00 00 00 ba d0 00 00 28 00 00 00 6e 04 00 00 40 03 |

With the bytes now corrected the file should open with flag printed on image
> eog tunn3l_v1s10n
