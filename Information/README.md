# Wave A Flag

## FLAG: picoCTF{the_m3tadata_1s_modified}

## STATUS: Complete

Category: forensics
Description: Files can always be changed in a secret way. Can you find the flag? cat.jpg

> wget "https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg"
> strings cat.jpg > cat-strings.txt
> exiftool cat.jpg

- ExifTool Version Number         : 12.40
    File Name                       : cat.jpg
    Directory                       : .
    File Size                       : 858 KiB
    File Modification Date/Time     : 2021:03:15 11:24:46-07:00
    File Access Date/Time           : 2022:03:17 13:49:24-07:00
    File Inode Change Date/Time     : 2022:03:17 13:48:57-07:00
    File Permissions                : -rw-r--r--
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    JFIF Version                    : 1.02
    Resolution Unit                 : None
    X Resolution                    : 1
    Y Resolution                    : 1
    Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
    Copyright Notice                : PicoCTF
    Application Record Version      : 4
    XMP Toolkit                     : Image::ExifTool 10.80
    License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
    Rights                          : PicoCTF
    Image Width                     : 2560
    Image Height                    : 1598
    Encoding Process                : Baseline DCT, Huffman coding
    Bits Per Sample                 : 8
    Color Components                : 3
    Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
    Image Size                      : 2560x1598
    Megapixels                      : 4.1

> xxd cat.jpg > hexdump-cat
> echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 --decode

- picoCTF{the_m3tadata_1s_modified}
