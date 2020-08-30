#include<stdio.h>
#include<unistd.h>
#include <stdlib.h>
#include<time.h>

#include <signal.h>

void delay_sec(int seconds)
{
	int milli = 1000 * seconds;
	clock_t start = clock();
	while(clock() < start + milli )
		;

}

void child1()
{
	for (int i = 0; i < 10; ++i)
	{
		printf("message");
		sleep(1);

	}


}

void child2(int n)
{	
	
	sleep(10);
	kill(n,1);
	sleep(10);
	exit(0);
}


int main()
{
		int c1,c2,d1,d2;

		//child 1
		int n1 = fork();
		if(n1 == 0)
		{	 c1 = getpid();
			 d1 = getppid();
			//printf("child = %d and parent = %d\n",c1,d1 );
			child1();
			exit(0);
		
		}

		//child 2
		int n2 = fork();
		if(n2 == 0)
		{	  c2 = getpid();
			  d2 = getppid();
			//printf("child = %d and parent = %d\n",c2,d2 );
			  child2(c1);

			
		
		}
	

		exit(0);
		

	/*for (int i = 0; i < 2; ++i)
	{
		wait(0);
	}*/


}