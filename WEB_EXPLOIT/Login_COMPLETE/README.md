# Login

## FLAG: picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}

## Status: Incomplete

Category: Web-Exploit

Description: My dog-sitter's brother made this website but I can't get in; can you help?
login.mars.picoctf.net

## STEPS

1. Navigate to website
2. Inspect page
   1. There is a static js file
   2. Download and run through beautifier
3. Looking as js file we see a validation portion that checks the username and password
   1. UN: `YWRtaW4`
   2. PW: `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ`
   3. This looks like base64
4. Base64 Decode
   1. > echo "YWRtaW4" | base64 -d
      1. RESPONSE: `admin`
   2. > echo "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" | base64 -d
      1. RESPONSE: `picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`
5. Tested Credentials = SUCESS
