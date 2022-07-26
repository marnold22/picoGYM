# File-Run2

## FLAG: picoCTF{F1r57_4rgum3n7_f65ed63e}

## Status: Complete

Category: Reverse-Engineer

Description: Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input 'Hello!'? Download the program here.

## STEPS

1. wget <https://artifacts.picoctf.net/c/353/run>
2. strings `run`
   1. Output: `picoCTF{F1r57_4rgum3n7_f65ed63e}`