# Who-Are-You

## FLAG: picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_0da16bb2}

## Status: Complete

Category: Web-Exploit

Description: Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn <http://mercury.picoctf.net:36622/>

## RESOURCES

1. HTTP Header Options
   1. <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>
2. IP Locations (for Sweden)
   1. <https://lite.ip2location.com/sweden-ip-address-ranges?lang=en_US>

## STEPS

1. Navigate to website
   1. > curl <http://mercury.picoctf.net:36622/>
   2. "Only people who use the official PicoBrowser are allowed on this site!"
2. Let's try modifying the headers using a python script -> solve.py
   1. "Only people who use the official PicoBrowser are allowed on this site!"
      1. Change the `User-Agent`
   2. "I don't trust users from another site"
      1. Change the `Referer`
   3. "Sorry, this site only worked in 2018"
      1. Change the `Date`
   4. "I don't trust users who can be tracked"
      1. Change the `DNT` (Do Not Track)
   5. "This website is only for people from Sweden"
      1. Change `X-Forwarded-For` this uses ip address from a location
   6. "You're in Sweden but you don't speak Swedish?"
      1. Change `Accept-Language`
   7. `picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_0da16bb2}`
