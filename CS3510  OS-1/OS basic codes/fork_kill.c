#include<stdio.h>
#include<sys/types.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>
#include<signal.h>

int main()
{
	int pid;  // pid_t pid;
	char buf[100];

	int ret = fork();
	printf("return value of fork : %d\n",ret );
	pid = getpid();
	
	for (int i = 1; i <=5; i++)
	{
		write(1,buf , strlen(buf));
		printf("Pid is %d\n", pid  );
		if(i==3 && ret == 0)
		{
			printf("Child process is killed\n");
			int a = kill(pid,SIGKILL);
			
		}
		
	}
}
