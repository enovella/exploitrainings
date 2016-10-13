#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    volatile int modified;
    char buffer[64];
    
    if (argc == 1) {
        errx(1, "Please specify an argument!\n");
    }
    
    modified = 0;
    strcpy(buffer, argv[1]);
    
    if (modified == 0x61626364) {
        printf("You have correctly got the variable to the right value!\n");
    } else {
        printf("Try again, you got 0x%08x\n", modified);
    }
    
    return 0;
}
