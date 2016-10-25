.section .text
	.globl _start
_start:
  mov  $0, %eax
  push %eax

  push $0x68732f2f
  push $0x6e69622f
  mov  %esp, %ebx
  push %eax
  mov %esp, %edx
  push %ebx
  mov %esp, %ecx
  mov $11, %eax
  int  $0x80
