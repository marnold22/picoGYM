# Nice Netcat

## FLAG: picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}

## STATUS: Complete

Category: general skills

Description: There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449 but it doesn't speak English

Hint-1: You can practice using netcat with this picoGym problem: what's a netcat? <https://play.picoctf.org/practice/challenge/34>
Hint-2: You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up <https://play.picoctf.org/practice/challenge/22>

> nc mercury.picoctf.net 7449
> nc mercury.picoctf.net 7449 > response

Then need to run getFlag.py which converts list of ascii values into characters
