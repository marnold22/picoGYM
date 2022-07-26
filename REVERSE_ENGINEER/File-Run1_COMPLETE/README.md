# File-Run1

## FLAG: picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}

## Status: Complete

Category: Reverse-Engineer

Description: A program has been provided to you, what happens if you try to run it on the command line?
Download the program here.

## STEPS

1. wget <https://artifacts.picoctf.net/c/310/run>
2. file run
   1. `ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked`
3. open ghidra to anaylze code
   1. In main() function we see a call to print(flag, flag)
   2. Clicking on flag we see on the stack `picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}`
4. Other option is to run `strings` command on the run file
   1. Searchin gthe output we see: `picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}`