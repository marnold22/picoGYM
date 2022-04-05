# ARMssembly-0

## FLAG: picoCTF{e5c69cd8}

## STATUS: Complete

Category: Reverse-Engineering

Description: What integer does this program print with arguments `3854998744` and `915131509`? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

> wget "https://mercury.picoctf.net/static/b3b17204c7ce77f184a397c4fae4a35b/chall.S"

## COMPILE TESTS

> nasm -f elf64 chall.s
> nasm -f elf64 chall.asm
> gcc chall.s -no-pie -o chall

After inspecting the assembly file it shows armv8-a which leads me to think I need to use an ARM based compiler

> sudo apt install gcc-aarch64-linux-gnu
> aarch64-linux-gnu-gcc chall.S

## NEED HELP - CREDIT to xnomas (NONE OF THE COMPILING IS NEEDED!!!)

<https://ctftime.org/writeup/26962>

Understanding the basics

sp stands for the stack pointer, and the sub instruction is a substraction with three components:
sub x,y, #z
Substract #z (# denotes a constant value) fro y and store it in x. Why is this instruction even here? It makes space on the stack for variables, and since we have two, substracting 16 should be just enough. In the next two lines we have some essential instructions:
str w0, [sp, 12]  
str w1, [sp, 8]
str stands for store, and w0 and w1 are the user input variables. So we store the values in w0 and w1 on the stack (sp). The number denotes the offset on the stack. So str w0, [sp, 12] means store w0 on the stack at offset 12. Pretty neat.
ldr w1, [sp, 12]
ldr w0, [sp, 8]
Here we load the values from the stack at a given offset into a variable. So load the value at offset 12 on the stack into w1 is equal to ldr w1, [sp, 12]. Also neat! And very important.
cmp w1, w0
Compare the values by substracting w0 from w1. So basically a sub except that we do not store the value. Next!
bls .L2
Right, this is a branch if less instruction, if w0 is smaller than w1 branch or jl (for the x86 guys) to .L2. And at the end load a value again and b (simple branch jmp in x86). Very nice!

Remaining functions
.L2:
    ldr w0, [sp, 8]  
.L3:
    add sp, sp, 16
    ret
    .size   func1, .-func1
    .section    .rodata
    .align  3

At .L2 we load a value from the stack at offset 8 into the variable w0 and continue execution back in func1. In .L3 we just add 16 back to sp, ie. we fill the stack back again.

Here is the main function with my added "comments". So if we add everything together, what happens? If we just skip to the important bit, before branching to .L3 the value from [sp, 12] is loaded and printed! So what is the flag?

Convert 3854998744 into a 32 bit hex string and that is it.

## GET FLAG

Convert 3854998744 into a 32 bit hex string
Use my poc.py script
