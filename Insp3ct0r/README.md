# Insp3ct0r

## FLAG: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}

## Status: Complete

Category: Web-Exploit

Description: Kishor Balan tipped us off that the following code may need inspection: <https://jupiter.challenges.picoctf.org/problem/44924/> (link) or <http://jupiter.challenges.picoctf.org:44924>

Hint-1: How do you inspect web code on a browser?
Hint-2: There's 3 parts

> wget "https://jupiter.challenges.picoctf.org/problem/44924/"

After inspecting the html code we can see there is also a static css file `mycss.css` and a static js file `myjs.js` so we will pull these down too

> wget "https://jupiter.challenges.picoctf.org/problem/44924/mycss.css"
> wget "https://jupiter.challenges.picoctf.org/problem/44924/myjs.js"

After insopecting each file, they all have commented code out with each containing 1/3 of the flag

HTML - Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3
CSS - You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t
JS - Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?f10be399}

AFter combining all the pieces we now have a full flag: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
