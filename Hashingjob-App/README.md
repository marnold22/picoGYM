# Hashingjob-App

## FLAG: picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}

## Status: Complete

Category: General-Skills

Description: If you want to hash with the best, beat this test! nc saturn.picoctf.net 5768

## STEPS

1. > nc saturn.picoctf.net 5768
   1. `Please md5 hash the text between quotes, excluding the quotes: 'a schoolbus'`
   2. ANSWER: ______
2. > md5 -s "STRING_HERE" (or md5sum if on linux)
   1. RESPONSE: 08ff1bc7567f9bd3362e6e4cdc11320f
3. Re-run program

   ```Text
    Please md5 hash the text between quotes, excluding the quotes: 'a schoolbus'
        Answer:
            dfafe30768c4ded89ca210e239682514
            dfafe30768c4ded89ca210e239682514
        Correct.
    Please md5 hash the text between quotes, excluding the quotes: 'leeches'
        Answer:
            1719980de08011881ae8f13c90baaa92
            1719980de08011881ae8f13c90baaa92
        Correct.
    Please md5 hash the text between quotes, excluding the quotes: 'Alfred Hitchcock'
        Answer:
            e205d7c24a5780f9eeb2315049febe0b
            e205d7c24a5780f9eeb2315049febe0b
        Correct.
    picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}
   ```

4. Here is our flag `picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}`
