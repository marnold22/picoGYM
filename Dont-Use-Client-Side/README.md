# Dont-Use-Client-Side

## FLAG: picoCTF{no_clients_plz_7723ce}

## Status: Complete

Category: Web-Exploit

Description: Can you break into this super secure portal? <https://jupiter.challenges.picoctf.org/problem/29835/> (link) or <http://jupiter.challenges.picoctf.org:29835>

## STEPS

1. Navigate to website & open dev tools
2. upon inspcetion we see a script

    ```js
    function verify() {
        checkpass = document.getElementById("pass").value;
        split = 4;
        if (checkpass.substring(0, split) == 'pico') {
        if (checkpass.substring(split*6, split*7) == '723c') {
            if (checkpass.substring(split, split*2) == 'CTF{') {
            if (checkpass.substring(split*4, split*5) == 'ts_p') {
            if (checkpass.substring(split*3, split*4) == 'lien') {
                if (checkpass.substring(split*5, split*6) == 'lz_7') {
                if (checkpass.substring(split*2, split*3) == 'no_c') {
                    if (checkpass.substring(split*7, split*8) == 'e}') {
                    alert("Password Verified")
                    }
                    }
                }
        
                }
            }
            }
        }
        }
        else {
        alert("Incorrect password");
        }
        
    }
    ```

3. This script looks like it is "verifying" the password on the "Client Side" and is parsing the string in chunks of 4
4. Breaking it apart and re-aranging it we see

    ```js
    (0, split) == 'pico'
    (split, split*2) == 'CTF{'
    (split*2, split*3) == 'no_c'
    (split*3, split*4) == 'lien'
    (split*4, split*5) == 'lien'
    (split*5, split*6) == 'lz_7'
    (split*6, split*7) == '723c'
    (split*7, split*8) == 'e}'
    ```

5. Extrsacting just the string (text value) we get: `picoCTF{no_clients_plz_7723ce}`
