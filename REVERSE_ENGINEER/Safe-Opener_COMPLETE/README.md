# Safe-Opener

## FLAG: picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

## Status: Complete

Category: Reverse-Engineer

Description: I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

## STEPS

1. wget <https://artifacts.picoctf.net/c/463/SafeOpener.java>
2. examining the code we see this chunk

    ```java
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
    ```

3. Run this through base64 decode

    ```bash
    echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
    ```

4. OUTPUT: `pl3as3_l3t_m3_1nt0_th3_saf3`
