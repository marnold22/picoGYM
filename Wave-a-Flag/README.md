# Wave A Flag

## FLAG: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}

## STATUS: Complete

Category: general skills

Description: Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

Hint-1: This program will only work in the webshell or another Linux computer.
Hint-2: To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`
Hint-3: Run this program by entering the following in the Terminal prompt: `$ ./warm, but you'll first have to make it executable with $ chmod +x warm`
Hint-4: -h and --help are the most common arguments to give to programs to get more information from them!
Hint-5: Not every program implements help features like -h and --help.

> wget "https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm"
> file warm

- ELF 64-bit LSB pie executable

> strings warm

- Hello user! Pass me a -h to learn what I can do! Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}

> chmod +x warm
> ./warm
> ./warm -h

- Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
