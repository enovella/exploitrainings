#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win()
{
    printf("Code flow successfully changed!\n");
}

int main(int argc, char **argv)
{
    volatile int (*fp)();
    char buffer[64];
    fp = 0;
    
    gets(buffer);
    
    if (fp) {
        printf("Calling function pointer, jumping to 0x%08x\n");
        fp();
    }
    
    return 0;
}
