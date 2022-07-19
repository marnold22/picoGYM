# Logon

## FLAG: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}

## Status: Complete

Category: Web-Exploit

Description: The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? <https://jupiter.challenges.picoctf.org/problem/15796/> (link) or <http://jupiter.challenges.picoctf.org:15796>

## STEPS

UN: Joe

1. Navigate to the webpage
2. Can login without any credentials but shows `NO FLAG FOR YOU`
3. Try Logging in as Joe
4. In developer tools we see cookies being set for username: joe, password: (USERINPUT), admin: False
5. By altering the cookie to be `admin: True`
6. Now reloading the page give us: `FLAG: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}`
