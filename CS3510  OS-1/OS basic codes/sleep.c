#include <stdio.h>
#include <unistd.h>

int main() 
{
    pid_t pid1 = getpid();
    for(int i = 0;i < 3;i++)
    {
        printf("Pid : %d\n",pid1 );
        fflush(stdout);
        sleep(1);
    }
}