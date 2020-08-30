#include<stdio.h>
#include<sys/types.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>
#include<signal.h>


int main()
{
	int pid = getpid();
	printf("Inital parent process pid : %d and its parent PID : %d\n" , pid ,getppid() );
	int ret = fork();
	//printf("fork return value : %d \n" , ret);
	int pid1 = getpid();
	if(ret == 0)
	{printf("child process pid : %d and its parent PID : %d \n" , pid1 ,getppid());}
}

 
