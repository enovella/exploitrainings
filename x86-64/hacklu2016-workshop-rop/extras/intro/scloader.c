/*
** scloader.c for exploitation course
**
** Made by Julien Bachmann
**
** Started on  Wed Apr 11 21:54:58 2012 Julien Bachmann
** Last update Wed Apr 22 20:42:40 2015 Julien Bachmann
*/

// Note: -fno-stack-protector -z execstack

#include <stdio.h>
#include <string.h>

int     main(int argc, char** argv)
{
  if (argc != 2)
  {
    printf("usage: %s <shellcode>\n", argv[0]);
    return 1;
  }
  ((void (*)(void))(argv[1]))();
  return 0;
}
