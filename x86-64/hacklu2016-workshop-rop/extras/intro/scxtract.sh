#!/bin/bash
let COUNT=0
MSC=""
for x in `objdump -d $1 | grep -o -P '\t([0-9a-f][0-9a-f] )*'`
do
	let COUNT=$COUNT+1
	MSC="${MSC}\x${x}"
done
echo "Size : $COUNT"
echo "${MSC}"
