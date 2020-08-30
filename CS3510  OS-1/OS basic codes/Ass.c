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
  
  int ch1 , ch2;
  ch1 = fork();
  pid_t pid1 = getpid();
  


  if(ch1 != 0)
  {
    ch2 = fork();
    pid_t pid2 = getpid();

    if(ch2 == 0 )
    {
      printf("child 2(PID : %d) sleeping ...\n",pid2);
      sleep(10);
      printf("child 2(PID : %d) woke up after 10 secs ...\n",pid2);
      kill(ch1 , SIGKILL);
      printf("Child 2 killed child 1\n");
      sleep(10);
    }
    else
    {
      waitpid(ch2 , NULL , 0);
      printf("child 2 is terminated\n");
      printf("Parent Process is exiting\n");
      exit(0);
    }
  }


  else
  {
    
    for (int i = 0; i < 10; ++i)
    {
      
      printf("Child 1 with PID =   %d\n",pid1);
      sleep(1);
      fflush(stdout);
      
    }
  }

  



}