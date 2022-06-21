# Spelling-Quiz

## FLAG: picoCTF{perhaps_the_dog_jumped_over_was_just_tired}

## Status: Complete

Category: Cryptography

Description: I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.

## STEPS

1. > wget <https://artifacts.picoctf.net/picoMini+by+redpwn/Cryptography/spelling-quiz/public.zip>
2. > unzip public.zip

## NEED HELP - CREDIT: <https://www.ctfwriteup.com/picoctf/picomini-by-redpwn/cryptography>

1. Run python script to analyze letter frequency
   1. We see `r` is the most common so lets substitute `e`
2. Quipquip
   1. Input encoded flag
   2. Substitute `r=e`
   3. Run tools
      1. RESPONSE: `perhaps_the_dog_jumped_over_was_just_tired`
