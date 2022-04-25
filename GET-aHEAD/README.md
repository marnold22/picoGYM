# GET-aHEAD

## FLAG: picoCTF{r3j3ct_th3_du4l1ty_775f2530}

## STATUS: Complete

Category: Web-Exploit

Description: Find the flag being held on this server to get ahead of the competition <http://mercury.picoctf.net:45028/>

Hint-1: Maybe you have more than 2 choices
Hint-2: Check out tools like Burpsuite to modify your requests and look at the responses

Used Burp Suite to intercept proxy traffic at <http://mercury.picoctf.net:45028/>

Modified HTTP request type from GET, POST, HEAD, PUT, DELETE

after trying all - HEAD returned the flag in the header content

{'flag': 'picoCTF{r3j3ct_th3_du4l1ty_775f2530}', 'Content-type': 'text/html; charset=UTF-8'}
