# Serpentine

## FLAG: picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}

## Status: Complete

Category: General-Skills

Description: Find the flag in the Python script!
Download Python script

## STEPS

1. > wget <https://artifacts.picoctf.net/c/93/serpentine.py>
2. > python3 serpentine.py
   1. Choose option B
      1. RESPONSE: `Oops! I must have misplaced the print_flag function! Check my source code!`
3. Edit Python Script

    ```py
        elif choice == 'b':
            print_flag()
            # print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
    ```

4. > python3 serpentine.py
   1. Choose option B
      1. RESPONSE: `picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}`
