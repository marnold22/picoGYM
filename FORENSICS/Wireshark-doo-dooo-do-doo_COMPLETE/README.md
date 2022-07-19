# Wireshark-doo-dooo-do-doo

## FLAG: picoCTF{p33kab00_1_s33_u_deadbeef}

## Status: Complete

Category: Forensics

Description: Can you find the flag? shark1.pcapng

> wget "https://mercury.picoctf.net/static/ae5b2bc07928fca272ff3900dc9a6cef/shark1.pcapng"

Open the pcap file with wireshark
Found this in the wireshark pcap which looks to follow the picoCTF{xxxxxxxxxx} format:

Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}

After plugging this into a rot13 decoder we get:

The flag is picoCTF{p33kab00_1_s33_u_deadbeef}
