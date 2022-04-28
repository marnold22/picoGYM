undefined8 main(undefined8 argc, char **argv)
{
    undefined8 uVar1;
    int64_t in_FS_OFFSET;
    char **var_c0h;
    int64_t var_b4h;
    undefined var_a1h;
    int32_t var_a0h;
    int32_t var_9ch;
    void *var_98h;
    char *ptr;
    undefined8 stream;
    char *var_80h;
    char *s;
    char *var_70h;
    int64_t var_68h;
    int64_t var_60h;
    int64_t var_58h;
    char *s2;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    sym.imp.setbuf(_reloc.stdout, 0);
    stream = sym.imp.fopen("flag.txt", 0x400b08);
    sym.imp.fgets(&s2, 0x40, stream);
    var_70h = (char *)0x2073692073696874;
    var_68h = 0x6d6f646e61722061;
    var_60h = 0x2e676e6972747320;
    var_58h._0_1_ = 0;
    var_98h = (void *)0x0;
    for (var_9ch = 0; var_9ch < 7; var_9ch = var_9ch + 1) {
        ptr = (char *)sym.imp.malloc(0x80);
        if (var_98h == (void *)0x0) {
            var_98h = ptr;
        }
        *(undefined8 *)ptr = 0x73746172676e6f43;
        *(undefined8 *)((int64_t)ptr + 8) = 0x662072756f592021;
        *(undefined8 *)((int64_t)ptr + 0x10) = 0x203a73692067616c;
        *(undefined *)((int64_t)ptr + 0x18) = 0;
        sym.imp.strcat(ptr, &s2, &s2);
    }
    var_80h = (char *)sym.imp.malloc(0x80);
    *(undefined8 *)var_80h = 0x5420217972726f53;
    *(undefined8 *)((int64_t)var_80h + 8) = 0x276e6f7720736968;
    *(undefined8 *)((int64_t)var_80h + 0x10) = 0x7920706c65682074;
    *(undefined4 *)((int64_t)var_80h + 0x18) = 0x203a756f;
    *(undefined *)((int64_t)var_80h + 0x1c) = 0;
    sym.imp.strcat(var_80h, &var_70h, &var_70h);
    sym.imp.free(ptr);
    sym.imp.free(var_80h);
    var_a0h = 0;
    var_a1h = 0;
    sym.imp.puts("You may edit one byte in the program.");
    sym.imp.printf("Address: ");
    sym.imp.__isoc99_scanf(0x400b48, &var_a0h);
    sym.imp.printf("Value: ");
    sym.imp.__isoc99_scanf(0x400b53, &var_a1h);
    *(undefined *)((int64_t)var_a0h + (int64_t)var_98h) = var_a1h;
    s = (char *)sym.imp.malloc(0x80);
    sym.imp.puts(s + 0x10);
    uVar1 = 0;
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
        uVar1 = sym.imp.__stack_chk_fail();
    }
    return uVar1;
}