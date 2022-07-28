#!/usr/bin/env python3

cipher = "The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3"
rail = 4

enc=[[" " for i in range(len(cipher))] for j in range(rail)]

flag = 0
row = 0

for i in range(len(cipher)):
  enc[row][i]=cipher[i]
  if row==0:
    flag=0
  elif row==rail-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1

for i in range(rail):
  print("".join(enc[i]))