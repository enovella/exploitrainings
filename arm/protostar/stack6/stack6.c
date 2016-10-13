#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void getpath()
{
    char buffer[64];
    unsigned int ret;
    
    printf("Input path please: "); fflush(stdout);
    
    gets(buffer);
    
    ret = __builtin_return_address(0);
    
    if ((ret & 0xbe000000) == 0xbe000000) {
        printf("Bzzzt (%p) \n", ret);
        _exit(1);
    }
    
    printf("Got path: %s\n", buffer);
}

int main(int argc, char **argv)
{
    getpath();
    
    return 0;
}
