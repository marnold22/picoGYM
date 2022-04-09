# Scavenger-Hunt

## FLAG: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}

## Status: Incomplete

Category: Web-Exploit

Description: There is some interesting information hidden around this site <http://mercury.picoctf.net:5080/> Can you find it?

> wget "http://mercury.picoctf.net:5080/"
> wget "http://mercury.picoctf.net:5080/mycss.css"
> wget "http://mercury.picoctf.net:5080/myjs.js"

Each file containted 1/3 of the flag
HTML - picoCTF{t
CSS - h4ts_4_l0
JS - had a hint regarding "How can I keep Google from indexing my website?" this promted a google search.

GOOGLE:
using a meta tag or robots.txt

> wget "http://mercury.picoctf.net:5080/robots.txt"

User-agent: *
Disallow: /index.html
Part 3: t_0f_pl4c
I think this is an apache server... can you Access the next flag?

## HELP NEEDED CREDIT - Vivian-dai <https://github.com/vivian-dai/PicoCTF2021-Writeup>

> wget "http://mercury.picoctf.net:5080/.htaccess"

Part 4: 3s_2_lO0k
I love making websites on my Mac, I can Store a lot of information there.

> wget "http://mercury.picoctf.net:5080/.DS_Store"

Congrats! You completed the scavenger hunt. Part 5: _35844447}