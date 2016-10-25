#!/usr/bin/env python

from struct import pack

padding = 0 # find offset to overflow
junk = "A" * padding
 
## ROP gadgets ##
p = ''
# write ROP chain for executing /bin/sh

payload = junk + p
print payload
