.section 	.data
path:	.string "chiche"

.section 	.bss
.lcomm		buff, 512

.section 	.text
.global 	_start

_start:

mov 	$5,	%eax 	#syscall open
mov	$path, 	%ebx
mov 	$2,	%ecx	#rwrite / read 0 / write /1
int	$0x80

mov	%eax,	%esi

mov	%esi, 	%ebx	#mov le fd ds arg 1 de read
mov	$3,	%eax	#syscall read
mov	$buff,	%ecx
mov	$512,	%edx
int	$0x80

mov	%eax,	%edx	# nb carctere lu a write
mov	$4,	%eax	#syscall de write
mov	$1,	%ebx	# sortie standard
mov	$buff,	%ecx	#
int	$0x80


mov	$6,	%eax	#close
mov	%esi,	%ebx
int	$0x80

mov	$1,	%eax		#exit
mov	$42,	%ebx
int	$0x80
