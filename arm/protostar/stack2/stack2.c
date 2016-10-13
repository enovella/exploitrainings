#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char **argv)
{
    volatile int modified;
    char buffer[64];
    char *variable;
    
    variable = getenv("GREENIE");
    
    if(variable == NULL) {
        errx(1, "Please set the Greenie environment variable!\n");
    }
    
    modified = 0;
    
    strcpy(buffer, variable);
    
    if(modified == 0x0d0a0d0a) {
        printf("You have correctly modified the variabele\n");
    } else {
        printf("Try again, you got 0x%08x\n", modified);
    }
}
