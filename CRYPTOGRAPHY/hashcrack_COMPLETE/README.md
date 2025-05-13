# hashcrack

## FLAG: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_ce730f64}

## Status: Incomplete

Category: crytography

Description: A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

## STEPS

1. Access the server
   1. > nc verbal-sleep.picoctf.net 51759
   2. RESPONSE:

        ```text
            Welcome!! Looking For the Secret?
            We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
            Enter the password for identified hash:
        ```

        1. Lets go crack this
2. HACKSTATION
   1. Enter the hash
      1. RESULTS:
         1. 482c811da5d5b4bc6d497ffa98491e38 -> md5 -> `password123`
3. Go back and enter password
4. NEW HASH

    ```text
        Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
    ```

5. CRACKSTATION
   1. RESULTS:
      1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 -> sha1 -> `letmein`
6. NEW HASH

    ```text
        Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
    ```

7. CRACKSTATION
   1. RESULTS:
      1. 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 -> sha256 -> `qwerty098`
8. FLAG
   1. The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_ce730f64}