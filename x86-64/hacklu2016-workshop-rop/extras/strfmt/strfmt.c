/*
** Exploit exercice for CTF training session
** compile : gcc strfmt.c -Wall -Wextra -ansi -pedantic -m32 -Wl,-z,execstack -o strfmt
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_SIZE	40

void		vuln(char* input)
{
	char	local[MAX_SIZE + 1];

	if (strlen(input) > MAX_SIZE)
		exit(-1);
	strncpy(local, input, MAX_SIZE);
	printf(local);
	return;
}

int		main(int argc, char** argv)
{
	if (argc != 2)
		exit(-1);
	vuln(argv[1]);
	return 0;
}
