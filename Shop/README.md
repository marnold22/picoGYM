# Shop

## FLAG: picoCTF{b4d_brogrammer_591a895a}

## Status: Complete

Category: Reverse-Engineering

Description: Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 37799

Hint-1: Always check edge cases when programming

> wget "https://mercury.picoctf.net/static/e8e966fcaa1ff5ea48574046d0cf9c19/source"
> strings source > strings

For this challenge I need to obtain more coins to essentially buy the "fruitful flag"
To do this I "bought" a negative amount of items which returned positive coins. Then I proceeded to buy the flag.

The output was:
`Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 57 49 97 56 57 53 97 125]`

Ran ape.py to convert the ints to their ascii value characters
