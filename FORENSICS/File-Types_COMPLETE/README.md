# File-Types

## FLAG: picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}

## Status: Complete

Category: Forensics

Description: This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from here.

## STEPS

1. wget <https://artifacts.picoctf.net/c/325/Flag.pdf>
2. file flag.pdf
   1. Expected output: PDF Document
   2. Actual Output: shell archive text
   3. This tells me there is a potential file within a file
3. Anaylze Code
   1. In here we see `sed 's/^X//' << 'SHAR_EOF' | uudecode` upon examination the `uudecode` function decodes
1. mv Flag.pdf flag.sh
2. Run flag.sh
   1. ./flag.sh
3. See file type of newly generated flag file
   1. file flag: current ar archive
4. Change filetype to ar
5. binwalk -e flag.ar
6. file 64
   1. bzip2 compressed data, block size = 900k
7. bzip2 -d 64
8. Inspect newly extracted file
   1. file 64-> gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:41 2022, from Unix, original size modulo 2^32 326
   2. rename 64 to 64.gz
9.  gzip -d flag.gz
10. file 64
    1. lzip compressed data, version: 1
    2. rename to .lz
11. lzip -d 64.lz
12. Inspect new file
    1.  file 64 -> LZ4 compressed data (v1.4+)
    2.  rename to .lz4
13. lz4 -d 64.lz4
14. Inspect new file
    1.  file 64 -> LZMA compressed data, non-streamed, size 253
    2.  rename to 64.lzma
15. lzma -d 64.lzma
16. Inspect new file
    1.  file 64 -> lzop compressed data - version 1.040, LZO1X-1, os: Unix
    2.  rename to 64.lzop
17. lzop -d 64.lzop
18. Inspect new file
    1.  file 64 -> lzip compressed data, version: 1
    2.  rename to .lzip
19. lzip -d 64.lzip
20. Inspect new file
    1.  file 64.lzip.out -> XZ compressed data
    2.  rename to .xf
21. tar -xf 64.xz
    1.  Generated two files
        1.  7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
        2.  6630725f3062326375723137795f39353063346665657d0a
22. Cyberchef from hex
    1.  OUTPUT: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}`