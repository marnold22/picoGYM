# MacroHard-WeakEdge

## FLAG: picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## Status: Complete

Category: Forensics

Description: I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

> wget "https://mercury.picoctf.net/static/d3dd8cd51524d9fafcccd1b7d55f85e7/Forensics%20is%20fun.pptm"

> binwalk Forensics/ \is \fun.pptm
Inside the binwalk output we see a "hidden" folder

So we will extract all the data / files from the .pptm
> 7z x Forensics/ \is \fun.pptm

Under /ppt/slideMasters there is a hidden file
> file hidden
hidden: ASCII text, with no line terminators

> strings hidden
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q

Removed all the spaces and ran through base64 decode to get the flag
