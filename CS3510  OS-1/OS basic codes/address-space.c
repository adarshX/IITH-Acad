//  References : 1) https://www.geeksforgeeks.org/memory-layout-of-c-program/
//				 2) https://man7.org/linux/man-pages/man1/size.1.html
#include <stdio.h> 

int  A; // gloabal variable
int B = 5;

int main(void) 
{ 
	static int a;
	static int b = 1;
	int c = 2;
	return 0; 
} 

//
// Command : 1) gcc address-space.c -o prog_size
//			 2) size prog_size