void main(undefined4 param_1,undefined8 param_2)

{
  char cVar1;
  char acStack168 [24];
  undefined8 uStack144;
  undefined8 local_88;
  undefined4 local_7c;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined2 local_60;
  undefined local_5e;
  char *local_50;
  undefined8 local_48;
  ulong local_40;
  __gid_t local_34;
  ulong local_30;
  
  uStack144 = 0x40079c;
  local_88 = param_2;
  local_7c = param_1;
  setbuf(stdout,(char *)0x0);
  uStack144 = 0x4007a1;
  local_34 = getegid();
  uStack144 = 0x4007bb;
  setresgid(local_34,local_34,local_34);
  local_40 = 0x1b;
  local_78 = 0x20656d6f636c6557;
  local_70 = 0x636520796d206f74;
  local_68 = 0x6576726573206f68;
  local_60 = 0x2172;
  local_5e = 0;
  local_48 = 0x1a;
  local_50 = acStack168;
  for (local_30 = 0; local_30 < local_40; local_30 = local_30 + 1) {
    cVar1 = convert_case((int)*(char *)((long)&local_78 + local_30),local_30);
    local_50[local_30] = cVar1;
  }
  puts(local_50);
  do {
    do_stuff();
  } while( true );
}


void do_stuff(void)

{
  char cVar1;
  undefined local_89;
  char local_88 [112];
  undefined8 local_18;
  ulong local_10;
  
  local_18 = 0;
  __isoc99_scanf("%[^\n]",local_88);
  __isoc99_scanf(&DAT_0040093a,&local_89);
  for (local_10 = 0; local_10 < 100; local_10 = local_10 + 1) {
    cVar1 = convert_case((int)local_88[local_10],local_10);
    local_88[local_10] = cVar1;
  }
  puts(local_88);
  return;
}
