# ARMssembly-2

## FLAG: picoCTF{38b09064}

## Status: Complete

Category: Reverse-Engineering

Description: What integer does this program print with argument 1748687564? File: chall_2.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Hint-1: Loops

> wget "https://mercury.picoctf.net/static/225b8846edf2234e9ce85aaab176b062/chall_2.S"

ASSEMBLY-CODE:

```S
    func1:
        sub sp, sp, #32
        str w0, [sp, 12]
        str wzr, [sp, 24]
        str wzr, [sp, 28]
        b .L2
```

reserve 32 bytes on stack
store w0 (our value) -> stackpointer 12
store wzr (val = 0) -> stackpointer 24
store wzr (val = 0) -> stackpointer 28
So:
stack + 12 = 1748687564
stack + 24 = 0
stack + 28 = 0

ASSEMBLY-CODE:

```S
    .L2:
        ldr w1, [sp, 28]
        ldr w0, [sp, 12]
        cmp w1, w0
        bcc .L3
        ldr w0, [sp, 24]
        add sp, sp, 32
        ret
        .size func1, .-func1
        .section .rodata
        .align 3
```

load w1 value at stackpointer 28 (val = 0)
load w0 value at stackpointer 12 (val = 1748687564)
compare w1 & w0, (this is like sub_function just without saving the value as a variable rather it sets the carry-flag)
CASES:
    w1 < w0 set the `zero-flag` = 0 and `carry-flag` = 1 <- **THIS IS OUR LOOP CONDITION**
    w1 > w0 set the `zero-flag` = 0 and `carry-flag` = 0
    w1 = w0 set the `zero-flag` = 1 and `carry-flag` = 0
bcc -> branch if carry is clear
essentially this is saying:

```python
    while w1 >= w0:
        l3()
```

after loop ends load value at stackpoint 24 into w0

ASSEMBLY-CODE:

```S
    .L3:
        ldr w0, [sp, 24]
        add w0, w0, 3
        str w0, [sp, 24]
        ldr w0, [sp, 28]
        add w0, w0, 1
        str w0, [sp, 28]
```

load w0 at stackpointer 24
add_function -> w0 + 3
store w0 (add_function) value at stackpointer 24
load w0 at stackpointer 28
add_function -> w0 + 1
store w0 (add_function) value at stackpointer 28

So essentially this is saying, at each loop iteration load value at stackpoint 24 and add 3, then load value at stackpoint 28 and add 1. Do this until stackpoint 28 > stackpoint 12 (our input value)

ASSEMBLY-CODE:

```S
    .LC0:
        .string "Result: %ld\n"
        .text
        .align 2
        .global main
        .type main, %function
```

print out the "Result"

NOW WHAT?

## NEED HELP - CREDIT: xnomas @ <https://ctftime.org/writeup/26964>

Solving it

So what do we actually need to do? Well think about it... we just want to loop. But can we do this without looping? 1748687564 loops is quite a lot.... How about we just calculate 1748687564 * 3 since we know that 3 will be added everytime and this is what will be printed.

1748687564 * 3 = 5246062692

Now just turn into hex and... Well not so fast. It needs to be a 32bit number
See flag.py for conversion
