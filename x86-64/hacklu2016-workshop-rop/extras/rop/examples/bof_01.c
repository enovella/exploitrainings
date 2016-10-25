/*
** bof_01.c for exploitation course
**
** Made by Julien Bachmann
**
** Started on  Mon Apr 16 21:28:05 2012 Julien Bachmann
** Last update Thu Dec 11 08:53:17 2014 Julien Bachmann
*/

// Note: -fno-stack-protector -m32 -static

#include <stdio.h>
#include <string.h>

static void     vulnerable(char* input)
{
  char          buffer[128];

  strcpy(buffer, input);
  printf("user input: %s\n", buffer);
  return;
}

int     main(int argc, char** argv)
{
  if (argc != 2)
  {
    printf("usage: %s <message>\n", argv[0]);
    return 1;
  }
  vulnerable(argv[1]);
  return 0;
}
