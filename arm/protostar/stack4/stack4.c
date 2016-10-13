#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void win()
{
    printf("Code flow successfully changed\n");
}

int main(int argc, char **argv)
{
    char buffer[64];
    gets(buffer);
    
    return 0;
}
