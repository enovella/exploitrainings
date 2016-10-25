/*
** bof_01.c for exploitation course
**
** Made by Julien Bachmann
**
** Started on  Mon Apr 16 21:28:05 2012 Julien Bachmann
** Last update Fri 01 May 2015 12:36:59 AM PDT Julien Bachmann
*/

// Note: -fno-stack-protector -z execstack

#include <stdio.h>
#include <string.h>

#include "poison.h"

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
