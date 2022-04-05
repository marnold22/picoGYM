# Wave A Flag

## FLAG: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}

## STATUS: Complete

Category: general skills
Description: Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

> wget "https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm"
> file warm

- ELF 64-bit LSB pie executable

> strings warm

- Hello user! Pass me a -h to learn what I can do! Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}

> chmod +x warm
> ./warm
> ./warm -h

- Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
