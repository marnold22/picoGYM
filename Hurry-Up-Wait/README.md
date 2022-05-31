# Hurry-Up-Wait

## FLAG: picoCTF{d15a5m_ftw_0e74cd4}

## Status: Complete

Category: Reverse-Engineer

Description: svchost.exe

## STEPS

1. > wget <https://mercury.picoctf.net/static/fd201a72f0c75546e682537feac07c85/svchost.exe>
2. > file svchost.exe
   1. RESPONSE: LF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=dffd9a6bc115677c3b91a1497e6f38affeaf8f50, stripped
3. Open up file in ghidra and we see

    ```c
    void FUN_0010298a(void)
    {
    ada__calendar__delays__delay_for(1000000000000000);
    FUN_00102616();
    FUN_001024aa();
    FUN_00102372();
    FUN_001025e2();
    FUN_00102852();
    FUN_00102886();
    FUN_001028ba();
    FUN_00102922();
    FUN_001023a6();
    FUN_00102136();
    FUN_00102206();
    FUN_0010230a();
    FUN_00102206();
    FUN_0010257a();
    FUN_001028ee();
    FUN_0010240e();
    FUN_001026e6();
    FUN_00102782();
    FUN_001028ee();
    FUN_001023da();
    FUN_0010230a();
    FUN_0010233e();
    FUN_0010226e();
    FUN_001022a2();
    FUN_001023da();
    FUN_001021d2();
    FUN_00102956();
    return;
    }
    ```

4. With some ghidra magic I renamed all the fucntions as "l_num" resembling "letter_num" or which position the letter would be in

    ```c
    void FUN_0010298a(void)
    {
    ada__calendar__delays__delay_for(1000000000000000);
    l_1();
    l_2();
    l_3();
    l_4();
    l_5();
    l_6();
    l_7();
    l_8();
    l_9();
    l_10();
    l_11();
    l_12();
    l_11();
    l_14();
    l_15();
    l_16();
    l_17();
    l_18();
    l_15();
    l_19();
    l_20();
    l_21();
    l_22();
    l_3();
    l_9();
    l_22();
    l_23();
    return;
    }
    ```

5. Looking at the function "l_1()"

    ```c
    void l_1(void)
    {
    ada__text_io__put__4(&DAT_00102cd8,&DAT_00102cb8);
    return;
    }
    ```

6. In this wee see two parameters `DAT_00102cd8` and `DAT_00102cb8` - this is also what the rest of the functions look like
7. Following the first parameter `DAT_00102cd8` we see `00102cd8 70     ??     70h     p` which highlights the letter `p`
8. Let's build this out in a table...

    |  FUNC  |  VAL  |
    |--------|-------|
    | l_1()  |   p   |
    | l_2()  |   i   |
    | l_3()  |   c   |
    | l_4()  |   o   |
    | l_5()  |   C   |
    | l_6()  |   T   |
    | l_7()  |   F   |
    | l_8()  |   {   |
    | l_9()  |   d   |
    | l_10() |   1   |
    | l_11() |   5   |
    | l_12() |   a   |
    | l_11() |   5   |
    | l_14() |   m   |
    | l_15() |   _   |
    | l_16() |   f   |
    | l_17() |   t   |
    | l_18() |   w   |
    | l_15() |   _   |
    | l_19() |   0   |
    | l_20() |   e   |
    | l_21() |   7   |
    | l_22() |   4   |
    | l_3()  |   c   |
    | l_9()  |   d   |
    | l_22() |   4   |
    | l_23() |   }   |

9. Flag: `picoCTF{d15a5m_ftw_0e74cd4}`
