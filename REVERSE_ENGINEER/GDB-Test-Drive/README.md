# GDB-Test-Drive

## FLAG: picoCTF{}

## Status: Incomplete

Category: Reverse-Engineer

Description: Can you get the flag? Here are the testdrive instructions:

```text
    chmod +x gdbme
    gdb gdbme
    (gdb) layout asm
    (gdb) break *(main+99)
    (gdb) run
    (gdb) jump *(main+104)
```

## STEPS

1. > wget "https://artifacts.picoctf.net/c/117/gdbme"
2. > chmod +x gdbme
3. > gdb gdbme
4. GDB COMMANDS
    1. layout asm
    2. break *(main+99)
    3. run
    4. jump *(main+104)
