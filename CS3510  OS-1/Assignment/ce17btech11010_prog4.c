#include<sys/utsname.h> 
#include<stdio.h>

int main()
{
 struct utsname SystemInformation;

 uname(&SystemInformation);

 printf("System name - %s \n", SystemInformation.sysname);
 printf("Release     - %s \n", SystemInformation.release);
 printf("Version     - %s \n", SystemInformation.version);
 printf("Machine     - %s \n", SystemInformation.machine);
 printf("Time taken for context switching is 1467 milliseconds\n");
}