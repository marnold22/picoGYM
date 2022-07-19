# Wireshark-twoo-twooo-two-twoo

## FLAG: picoCTF{dns_3xf1l_ftw_deadbeef}

## Status: Complete

Category: Forensics

Description: Can you find the flag? shark2.pcapng.

## STEPS

1. > wget <https://mercury.picoctf.net/static/719e81d6fbb6b3157624268588fc0de8/shark2.pcapng>
2. > wireshark shark2.pcapng
3. Saw many false positives
   1. picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}
   2. picoCTF{bda69bdf8f570a9aaab0e4108a0fa5f64cb26ba7d2269bb63f68af5d98b98245}
   3. picoCTF{fe83bcb6cfd43d3b79392f6a4232685f6ed4e7a789c2ce559cf3c1ab6adbe34b}
   4. ...
   5. *There were about 89 total iterations of this*
4. Try new approach
5. Run tshark to get hierarchy
6. > tshark -qz io,phs -r shark2.pcapng

    ```text
    ===================================================================
    Protocol Hierarchy Statistics
    Filter: 

    eth                                      frames:4831 bytes:3355920
    ip                                     frames:4829 bytes:3355822
        tcp                                  frames:3276 bytes:3120750
        tls                                frames:71 bytes:115780
            tcp.segments                     frames:2 bytes:6576
        http                               frames:802 bytes:1879844
            tcp.segments                     frames:299 bytes:1605841
            mime_multipart                   frames:309 bytes:194144
            tcp.segments                   frames:309 bytes:194144
            data-text-lines                  frames:91 bytes:23987
            tcp.segments                   frames:90 bytes:23696
            xml                              frames:1 bytes:579
        udp                                  frames:1553 bytes:235072
        gquic                              frames:41 bytes:11668
        dns                                frames:1512 bytes:223404
    arp                                    frames:2 bytes:98
    ===================================================================
    ```

7. Let's try going to the website that they were trying to access with GET & POST
8. Following the UDP stream we see the traffic trying to access `http://www.reddshrimpandherring.com` so lets try to access it
9. > curl <http://www.reddshrimpandherring.com> -> Flag: cGljb0NURntmMXNoeV9zMXR1NHRpMG5fc2VsYmF0X3liYm9iX2VsdHRpbH0=
10. > echo "cGljb0NURntmMXNoeV9zMXR1NHRpMG5fc2VsYmF0X3liYm9iX2VsdHRpbH0=" | base64 -d
11. Return: picoCTF{f1shy_s1tu4ti0n_selbat_ybbob_elttil} ***THIS FLAG DID NOT WORK***  

## NEED HELP CREDIT: Dvd848 <https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Wireshark_twoo_twooo_two_twoo.md>

1. > tshark -nr shark2.pcapng -Y 'dns && ip.src == 192.168.38.104 && frame contains "local" && ip.dst==18.217.1.57' | awk '{ print $12 }' | awk -F. '{ print $1 }' | tr -d "\n"

2. RETURN: `cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==fQ==`
3. > echo "cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==fQ==" | base64 -d
4. RETURN: `picoCTF{dns_3xf1l_ftw_deadbeef}`
