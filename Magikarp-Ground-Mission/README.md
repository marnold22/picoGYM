# Magikarp-Ground-Mission

## FLAG: picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}

Category: General-Skills

Description: Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

> ssh ctf-player@venus.picoctf.net -p 55136
> UN:ctf-player
> PW:ee388b88

ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt

> cat 1of3.flag.txt
Output: picoCTF{xxsh_
> cat instructions-to-2of3.txt
Output: Next, go to the root of all things, more succinctly `/`
> cd /
> cat 2of3.flag.txt
Output: 0ut_0f_\/\/4t3r_
> cat cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
> cd ~
> cat 3of3.flag.txt
Output: 3ca613a1}
