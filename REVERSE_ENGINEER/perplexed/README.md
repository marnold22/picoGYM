# perplexed

## FLAG: picoCTF{}

## Status: Incomplete

Category: Reverse-Engineering

Description: Download binary

## STEPS

1. Download the binary
   1. "perplexed"
2. FILE INFO
   1. > file perplexed
      1. ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=85480b12e666f376909d57d282a1ef0f30e93db4, for GNU/Linux 3.2.0, not stripped
      2. So it looks like it is an executable binary
   2. > strings perplexed
      1. We see a few that stick out:
         1. Enter the password: 
         2. Wrong
         3. Correct!
      2. So it looks like we will need to enter the correct password
3. GHIDRA
   1. Lets open this up in ghidra and look for the functions where the password check is happening!
   2. main()

        ```c
            printf("Enter the password: ");
            fgets(local_118,0x100,stdin);
            local_c = check(local_118);
            bVar1 = local_c != 1;
            if (bVar1) {
            puts("Correct!! :D");
            }
            else {
            puts("Wrong :(");
            }
            return !bVar1
        ```

        1. So it looks like it executes the fgets() function on the variable local_118, 
           1. Looks at up to 256 characters (thats what hex -> decimal of 0x100 = 256)
        2. Then it runs the check() funciton on our local_118 variable
        3. Sets bVar1 to local_c but NOT= 1
        4. Checks if bVar1 = true or 1 -> if so CORRECT!
        5. Else WRONG!
   3. check() -> specifically lets look at this with Binary Ninja, (not ghidra) that way we get teh hex values of the symbols too

        ```c
            int64_t check(char* arg1)
            {
                if (strlen(arg1) != 0x1b)
                    return 1;
                
                int64_t var_58;
                __builtin_memcpy(&var_58, 
                    "\xe1\xa7\x1e\xf8\x75\x23\x7b\x61\xb9\x9d\xfc\x5a\x5b\xdf\x69\xd2\xfe\x1b\xed\xf4\xed\x67\xf4", 
                    0x17);
                int32_t var_1c_1 = 0;
                int32_t var_20_1 = 0;
                int32_t var_2c_1 = 0;
                
                for (int32_t i = 0; i <= 0x16; i += 1)
                {
                    for (int32_t j = 0; j <= 7; j += 1)
                    {
                        if (!var_20_1)
                            var_20_1 += 1;
                        
                        int32_t rax_17;
                        rax_17 = (arg1[var_1c_1] & 1 << (7 - var_20_1)) > 0;
                        
                        if (rax_17 != (*(&var_58 + i) & 1 << (7 - j)) > 0)
                            return 1;
                        
                        var_20_1 += 1;
                        
                        if (var_20_1 == 8)
                        {
                            var_20_1 = 0;
                            var_1c_1 += 1;
                        }
                        
                        if (var_1c_1 == strlen(arg1))
                            return 0;
                    }
                }
                
                return 0;
            }
        ```

        1. So it looks like we have hex values, and this is probably where out flag is at!
        2. It also looks like the flag must be 27 characters long to be even considered
4. REBUILD
   1. So now lets rebuild this same thing