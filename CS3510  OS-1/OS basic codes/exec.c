#include<stdio.h>
#include<sys/types.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>
#include<signal.h>
#include<time.h>
#include<wait.h>

int main()
{
	pid_t pid = getpid();
	printf("%s with pid = %d\n", "Initial Process started" , pid);
	char *args[] = {"Hola", NULL};
	printf("Calling sleep process created from sleep.c\n");
	int c  = execv("./sleep" , args);
	printf("Status of exec %d\n",c );
	


}