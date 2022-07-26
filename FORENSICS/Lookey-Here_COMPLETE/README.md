# Lookey-Here

## FLAG: picoCTF{gr3p_15_@w3s0m3_2116b979}

## Status: Complete

Category: Forensics

Description: Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data here.

## STEPS

1. wget <https://artifacts.picoctf.net/c/296/anthem.flag.txt>
2. file anthem.flag.txt
   1. UTF-8 Unicode text
3. grep -e "pico" anthem.flag.txt
   1. `we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}`
4. Grab just the flag: `picoCTF{gr3p_15_@w3s0m3_2116b979}`