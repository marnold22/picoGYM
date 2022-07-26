# Packets-Primer

## FLAG: picoCTF{p4ck37_5h4rk_01b0a0d6}

## Status: Complete

Category: Forensics

Description: Download the packet capture file and use packet analysis software to find the flag.

## STEPS

1. wget <https://artifacts.picoctf.net/c/201/network-dump.flag.pcap>
2. file network-dump.flag.pcap
   1. OUTPUT: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
3. strings network-dump.flag.pcap
   1. OUTPUT: `p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }`
   2. Remove spaces: `picoCTF{p4ck37_5h4rk_01b0a0d6}`

## Proper Procedure

1. Open pcap file in wireshark Or open tshark (CLI)
2. For this we will use wireshark
3. wireshark network-dump.flag.pcap
4. In the main pane click on the first action [SYN]
   1. Right click and follow `TPC Stream`
5. Another pane is opened and the flag is displayed: `p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }`
