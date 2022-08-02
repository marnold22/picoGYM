# Rail-Fence

## FLAG: picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}

## Status: Complete

Category: Cryptography

Description: A type of transposition cipher is the rail fence cipher, which is described here. Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

## SETUP / UNDERSTANDING

ENCODING

1. This particular cipher uses a Rail-Fence with which looks like the following (credit wikipedia)
2. Using the message example of: `WE ARE DISCOVERED RUN AT ONCE`
3. We can spread it over the 3 rails and get the following

    ```text
        W . . . E . . . C . . . R . . . U . . . O . . . 
        . E . R . D . S . O . E . E . R . N . T . N . E 
        . . A . . . I . . . V . . . D . . . A . . . C . 
    ```

4. The RAILS will look like this
    1. ie: RAIL1: `WECRUO`
    2. ie: RAIL2: `ERDSOEERNTNE`
    3. ie: RAIL3: `AIVDAC`
5. Now taking each rail seperately to encode the message we get: `WECRUO ERDSOEERNTNE AIVDAC` as the encoded message

## MATH / DECODING

1. N = number of rails (during encryption)
2. In general the cycle period can be defined as 2(N-1)
3. L = the length of the string to be decrypted
4. Now suppose L is a multiple of 2(N-1) then...
   1. K = (L)/(2(N-1))
   2. "One begins by splitting the ciphertext into strings such that the length of the first and last string is K and the length of each intermediate string is 2K" - wikipedia page
5. For the example text above
   1. L = 24
   2. K = 6
   3. Write each string on a separate line with spaces after each letter in the first and last line
      1. RAIL1: W E C R U O
      2. RAIL2: ERDSOEERNTNE
      3. RAIL3: A I V D A C
6. In this we can see the first rail and last rail have k letters (6) and the intermediate rail has 2k (12)
7. Now if L is NOT a multiple of 2(N-1) then we use padding
8. The equation now becomes:
   1. 1 = ( L + y ) / ( N + ( (N-1) * x) )
   2. Where x+1 = number of diagonals in decrypted rail
   3. Where y = number of empty spaces in the last diagonal

## STEPS

1. wget <https://artifacts.picoctf.net/c/274/message.txt>
2. Taking the encoded message text: `Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA` we can lay it out on the rails as the following
   1. RAIL1: `Ta`
   2. RAIL2: `_7N6DDDhlg:W3D_H3C31N__0D3ef`
   3. RAIL3: `sHR053F38N43D0F`
   4. RAIL4: `i33___NA`
3. MATH PART
   1. N = 4
   2. L = 56 so 2(N-1) is not a multple of L meaining we need to use padding
   3. Solve for x & y (plug in vlaues for N = 4 & L = 56)
      1. Let x = {1, 2, 3, ... Z where 4+3Z >= 56}
      2. $ x = 18 -> {56 \over 58}$
      $$ 1 = {L+y \over N + ((N-1) * x)} $$

      $$ 1 = {56+y \over 4 + ((4-1) * 18)} $$

      $$ 1 = {56+y \over 58} $$

      $$ y = {2} $$
   4. Therefore
         1. N = 4 Rails
         2. L = 56 Characters
         3. y = 2 empty characters (as padding) at the end
         4. x = 18 (18+1) Total diagonals

4. Run through online decoder <https://cryptii.com/pipes/rail-fence-cipher>
   1. 4 Rails, Maintain punctuation & Spaces
   2. `The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3`
