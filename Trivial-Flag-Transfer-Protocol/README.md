# Trivial-Flag-Transfer-Protocol

## FLAG: picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

## Status: Complete

Category: Forensics

Description: Figure out how they moved the flag.

> wget "https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng"

Run Wireshark:
I can see there are several .bmp files, a .deb file, and an isntructions.txt file

- program.deb
- picture1.bmp
- picture2.bpm
- picture3.bmp
- instructions.txt

> binwalk tftp.pcapng > binwalk_output

Extract files from the pcapng file (after binwalk)
> binwalk --dd='.*' tftp.pcapng

Examine what each file is:
> file *

Output:
1172014: data
121BCA9: data
124A2AC: rzip compressed data - version 89.67 (1263815251 bytes)
1272A40: data
12A0905: HPack archive data
12DD4B9: data
12F8:    XZ compressed data, checksum CRC32
13A713F: data
13AEE6:  PC bitmap, Windows 3.x format, 4032 x 3024 x 24, image size 36578304, resolution 5669 x 5669 px/m, cbSize 36578358, bits offset 54
13BEC27: data
1439584: data
1490107: data
14EAADD: rzip compressed data - version 90.73 (1432243550 bytes)
156AD55: VMware4 disk image
2105916: data
2DF5E:   PC bitmap, Windows 3.x format, 605 x 454 x 24, image size 824464, resolution 5669 x 5669 px/m, cbSize 824518, bits offset 54
2FD5636: PC bitmap, Windows 3.x format, 807 x 605 x 24, image size 1466520, resolution 5669 x 5669 px/m, cbSize 1466574, bits offset 54
3182AB7: data
4D12DA:  data
849B1B:  rzip compressed data - version 87.76 (1415270489 bytes)
90710B:  data
BADE27:  data
BB1CD2:  data
BBDA5B:  data
BC5927:  data
C82:     POSIX tar archive (GNU)
C82-0:   gzip compressed data, max speed, from Unix, original size modulo 2^32 108
E25BA8:  MS-DOS executable
E57996:  data

We want to examine the `PC bitmap` files first

- 13AEE6
- 2DF5E
- 2FD5636

Extract files from the pcapng file (after binwalk)
> binwalk -e tftp.pcapng

Examine what each file is:
> file *
1172014.sit: data
121BCA9.sit: data
1272A40.sit: data
12DD4B9.sit: data
12F8:        POSIX tar archive (GNU)
12F8.xz:     XZ compressed data, checksum CRC32
13A713F.sit: data
13BEC27.sit: data
1439584.sit: data
1490107.sit: data
2105916.sit: data
3182AB7.sit: data
C82.gz:      gzip compressed data, max speed, from Unix, original size modulo 2^32 108

Tried to unzip C82.gz but only get the md5sums file out which shows:

71bdab1263ab4b8d28f34afa5f0ab121  usr/bin/steghide
11db80c2a5dbb9c6107853b08aeacc49  usr/share/doc/steghide/ABOUT-NLS.gz
57deb17212483b49f89587180d4d67d4  usr/share/doc/steghide/BUGS
72c7831222483f5c6d96ac2a8ca7ad48  usr/share/doc/steghide/CREDITS
adbb29f44a5e5eefda3c3d756cc15ab1  usr/share/doc/steghide/HISTORY
fe7cac39a1a1ef0975d24dfcf02f09b7  usr/share/doc/steghide/LEAME.gz
85587b9213ca2301eb450aad574d5f87  usr/share/doc/steghide/Iaaaa64aaaaataaaaaaaaaaaaaaaaaauear
eecc8cPe/doc/steghide/CREDITS
aaadaaaaaaaaatof
d4d67d4  aa2CREdbb
faaa0eaaaa /eaa aaa6 cc8c6a01a/1a6a0sr/1aaaaaauear
eecc8cPe/doc/steghide/CREDITS
aaadaaaaaaaaatof
d4d67d4  aa2CREdbb
faaa0eaaaa /eaa aaa6 cc8c6a01a/1a6a0sr/1aaaaaauear
eecc8cPe/doc/steghide/CREDITS
aaadaaaaaaaaatof
d4d67d4  aa2CREdbb
faaa0eaaaa /eaa aaa6 cc8c6a01a/1a6a0sr/1aaaaaauear
eecc8cPe/doc/-aat5l1a6a0sr/1aaaaaauear
eecaa/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaLaaaaaa0eaaaaaa9aaaaaaaaaaaaa2La790a eeccU0eaaaae/Baaaaaasr/odbb
ea27d4
cPe/doc/sghi9aaaaeaa2Co a4aaa0er3941a6a8a7941a/8oB rbaat6e5aa8aaa4ard4aaa0p5ac/s1adfaa166b8fa918c8
fa1i9ab68daaaaaaaaaaaaaaaaaLaaaaaa0eTODO
09d7710e276a06c4a3f3bc8
b3b86a4aaaaaaaaaaaaaaaaaLaaaaaa0echangelog.Debi%

## CHANGING GEARS & APPROACH

You can export the tftp files from wireshark file -> export objects -> TFTP
Exported all files to wireshark folder & now let's examine these files

> cat instructions.txt
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

Ran through cyberchef: (tried base64, magic, rot13) -> answer was rot13
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

> cat plan
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
ROT13: I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS

Examine the bitmap images
picture1.bmp -> cliff / forest
picture2.bpp -> more forest / cliff
picture3.bmp -> hills with dogs

Ran StegSeek to bruteforce password
> stegseek picture1.bmp

Ran steghide info on all images with password="DUEDILIGENCE"
> steghide info picture1.bmp
NO RESULT
> steghide info picture2.bmp
NO RESULT
> steghide info picture3.bmp
Enter passphrase: DUEDILIGENCE
  embedded file "flag.txt":
    size: 40.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
> steghide extract -sf picture3.bmp
wrote extracted data to "flag.txt"
> cat flag.txt
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

## CLEANUP

Removed binwalk export folder as it was unnecessary
