# ARMssembly-1

## FLAG: picoCTF{}

## Status: Incomplete

Category: Reverse-Engineering

Description: For what argument does this program print `win` with variables 58, 2 and 3? File: chall_1.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Hint-1: Shifts

> wget "https://mercury.picoctf.net/static/1c8d50e39cf00d144e6a72119f68c16c/chall_1.S"

## THIS REQUIRES HELP BUT CONCEPTS ARE STILL TESTED IN APE.PY FILE

## GET HELP - Credit to xnomas at <https://ctftime.org/writeup/26963>

ASSEMBLY-CODE:
    func:
        sub sp, sp, #32
        str w0, [sp, 12]
        mov w0, 58
        str w0, [sp, 16]
        mov w0, 2
        str w0, [sp, 20]
        mov w0, 3
        str w0, [sp, 24]

Breaking this down we see:

- stack + 12 = user_input
- stack + 16 = 58
- stack + 20 = 2
- stack + 24 = 3

ASSEMBLY-CODE:

    ldr w0, [sp, 20]
    ldr w1, [sp, 16]
    lsl w0, w1, w0
    str w0, [sp, 28]

In this chunk we load the value at stackpoint 20 into w0 and the value at stackpoint 16 into w1

- w0 = 2
- w1 = 58
- Then perform a left bit shift ( 58 shifted left by 2)
- lsl = 232 stored at stackpointer 28

ASSEMBLY-CODE:

    ldr w1, [sp, 28]
    ldr w0, [sp, 24]
    sdiv w0, w1, w0
    str w0, [sp, 28]

In this we are now loading stackpoint 28 as w1 and stackpoint 24 as w0

- w1 = 232
- w0 = 3
- Then perform sdiv ( 232 // 3 )
- sdiv = 77 stored at stackpointer 28

ASSEMBLY-CODE:

    ldr w1, [sp, 28]
    ldr w0, [sp, 12]
    sub w0, w1, w0
    str w0, [sp, 28]

In this we are now loading stackpoint 28 as w1 and stackpoint 12 as w0

- w1 = 77
- w0 = user_input
- Then perform sub ( 77 - user_input )
- sub = X stored at stackpointer 28

ASSEMBLY-CODE: (MAIN FUNCTION)

    main:
        stp x29, x30, [sp, -48]!
        add x29, sp, 0
        str w0, [x29, 28]
        str x1, [x29, 16]
        ldr x0, [x29, 16]
        add x0, x0, 8
        ldr x0, [x0]
        bl atoi
        str w0, [x29, 44]
        ldr w0, [x29, 44]
        bl func
        cmp w0, 0
        bne .L4
        adrp x0, .LC0
        add x0, x0, :lo12:.LC0
        bl puts
        b .L6

In this we see the `cmp w0, 0` line which indicates we need the value w0 to be 0, otherwise we go to .L4, and in our case we need to get to .L2 as that is the `win` condition / function

So for w0 = 0, that means the vlaue after performing the `sub` function where it subtracts ( 77 - user_input) needs to be 0

THUS: our user_input needs to be 77 that way sub ( 77 - 77 ) = 0

So lets run our ape.py file using the value 77 to convert to hex
