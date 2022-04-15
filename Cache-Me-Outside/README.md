# Cache-Me-Outside

## FLAG: picoCTF{}

## Status: Incomplete

Category: Binary-Exploit

Description: While being super relevant with my meme references, I wrote a program to see how much you understand heap allocations. nc mercury.picoctf.net 10097 heapedit Makefile libc.so.6

> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/heapedit"
> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/Makefile"
> wget "https://mercury.picoctf.net/static/97a073d6009c8cbd05d03b91ac3a620b/libc.so.6"

## NOTES

- Makefile compiles the code and removes (rm) the heapedit file
- Glib tcache research <https://guyinatuxedo.github.io/29-tcache/tcache_explanation/index.html>

Tried running heapedit but here is the error
> ./heapedit
`[1]    713 segmentation fault  ./heapedit`

## NEED HELP - CREDIT Dvd848 <https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Cache_Me_Outside.md>
