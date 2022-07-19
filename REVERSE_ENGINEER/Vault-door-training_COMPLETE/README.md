# Vault-door-training

## FLAG: picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}

## Status: Complete

Category: Reverse-Engineering

Description: Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: VaultDoorTraining.java

Hint-1: The password is revealed in the program's source code.

> wget "https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java"

This line of code: `String input = userInput.substring("picoCTF{".length(),userInput.length()-1);` from the source code shows thatthe user's input is used as an upperbound -1 for substring().

Later in the code it shows: `return password.equals("return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");");` which gives us the internal part of the flag.

However, based on the first part we know because leng() - 1 is used, we need an extra character at the end of the flag's "internal" chunk. Thus we need to use picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18} as the full input value.

Once running the java file
> java VaultDoorTraining.java
> Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}
> Access Granted.
