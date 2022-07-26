# Morse-Code

## FLAG: picoCTF{WH47_H47H_90D_W20U9H7}

## Status: Complete

Category: Cryptography

Description: Morse code is well known. Can you decrypt this?
Download the file here. Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

## STEPS

1. wget <https://artifacts.picoctf.net/c/235/morse_chal.wav>
2. file morse_chal.wav
   1. RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
3. Run audio file through online morse-code converter <https://morsecode.world/international/decoder/audio-decoder-adaptive.html>
   1. OUTPUT: `WH47 H47H 90D W20U9H7`
   2. Remove spaces, add _, and wrap in picoCTF{}
   3. `picoCTF{WH47_H47H_90D_W20U9H7}`