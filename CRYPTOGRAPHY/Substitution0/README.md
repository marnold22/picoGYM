# Substitution0

## FLAG: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}

## Status: Complete

Category: Crytography

Description: A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?

## TASKS

1. wget <https://artifacts.picoctf.net/c/381/message.txt>
2. Being substitution cipher at the end of the message we see: `ieuwUYJ{5FO5717F710K_3A0CF710K_357OJ9JJ}`
3. Let's try substituting i -> p and e -> i as those are the first two characters in `picoCTF`
4. Run through QUIPQUIP.com
5. OUTPUT

    ```text
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Hereupon Legrand arose, with a grave and stately air, and brought me the beetle from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at that time, unknown to naturalists—of course a great prize in a scientific point of view. There were two round black spots near one extremity of the back, and a long one near the other. The scales were exceedingly hard and glossy, with all the appearance of burnished gold. The weight of the insect was very remarkable, and, taking all things into consideration, I could hardly blame Jupiter for his opinion respecting it. 
        The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}
    ```
