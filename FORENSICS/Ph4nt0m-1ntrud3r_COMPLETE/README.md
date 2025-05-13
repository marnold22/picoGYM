# Ph4nt0m-1ntrud3r

## FLAG: picoCTF{1t_w4snt_th4t_34sy_tbh_4r_e5e8c78d}

## Status: Complete

Category: Forensics

Description: A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder

## STEPS

1. Download PCAP file
   1. "myNetworkTraffic.pcap"
2. WIRESHARK
   1. Lets open this up in wireshark and take a look
3. ANALYSIS
   1. So when we open up the pcap file we see a bunch of TCP traffic with several frames being TCP-Retransmission
   2. There are 22 frames
   3. When we click on each frame we get what looks like a snippet of base64 at the end of the data??
   4. The "Times" are all over the place - maybe we need to sort these by value
4. CRACK
   1. Sort the frames by time (in ascending order)
   2. Grab the snippets of each frame
      1. Negative Times:
         1. hWiUvqQ=
         2. w2iRHng=
         3. gVsRoPU=
         4. n0tn4jY=
         5. YZYAvEs=
         6. z3Iyzvg=
      2. Positive Times:
         1. BNAUd6U=
         2. gCjvy9o=
         3. +Zyh8zU=
         4. oZYrPGE=
         5. 2FljUAw=
         6. 5h7f9gw=
         7. QHESHGY=
         8. LpPuQ6w=
         9. G6UztJw=
         10. cGljb0NURg==
         11. ezF0X3c0cw==
         12. bnRfdGg0dA==
         13. XzM0c3lfdA==
         14. YmhfNHJfZQ==
         15. NWU4Yzc4ZA==
         16. fQ==
5. CYBERCHEF
   1. Decoding all of these from base64 we see something stick out in the 12len chunks
      1. BASE64 -> cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfZQ==NWU4Yzc4ZA==fQ==
         1. DECODED: `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_e5e8c78d}`






















