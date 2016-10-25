/*
** tp_rop.c for exploitation course
**
** Made by Julien Bachmann
**
*/

// Note: -fno-stack-protector -m32 -static

#include <stdio.h>
#include <string.h>

unsigned int    i = 0;
FILE*           f = NULL;

static void     usage(char* exec)
{
  printf("usage: %s <message>\n", exec);
}

static void     vulnerable(char* input, int size)
{
  char          buffer[240];

  memset(buffer, '\0', 240);
  f = fopen(input, "r");
  fread(buffer, size, sizeof (char), f);
  printf("user input: %s\n", buffer);
  fclose(f);
  return;
}

int     main(int argc, char** argv)
{
  if (argc != 3)
  {
    printf("usage: %s <file> <size>\n", argv[0]);
    return 1;
  }
  vulnerable(argv[1], atoi(argv[2]));
  return 0;
}
