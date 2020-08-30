#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define BUFSIZE 1024

int main(int argc, char **argv) {

	if (argc != 3) {
		perror("<Server Address> <Server Port>");
		exit(-1);
	}
	
	fputs("\t \t \t  ----- Client 1------ ",stdout);
	char *servIP = argv[1];
	char echoString[100];
	fputs("\t \t \t ",stdout);
	fgets(echoString,sizeof(echoString),stdin);


	in_port_t servPort = atoi(argv[2]);
	
	//Creat a socket
	int sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (sockfd < 0) {
		perror("socket() failed");
		exit(-1);
	}
	
	// Set the server address
	struct sockaddr_in servAddr;
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	int err = inet_pton(AF_INET, servIP, &servAddr.sin_addr.s_addr);
	if (err <= 0) {
		perror("inet_pton() failed");
		exit(-1);
	}
	servAddr.sin_port = htons(servPort);

	
	// Connect to server
	if (connect(sockfd, (struct sockaddr *) &servAddr, sizeof(servAddr)) < 0) {
		perror("connect() failed");
		exit(-1);
	}
	
	size_t echoStringLen = strlen(echoString);
	
	// Send string to server
	ssize_t sentLen = send(sockfd, echoString, echoStringLen, 0);
	if (sentLen < 0) {
		perror("send() failed");
		exit(-1);
	} else if (sentLen != echoStringLen) {
		perror("send(): sent unexpected number of bytes");
		exit(-1);
	}
	//fputs("\t \t \t \t \t \tClient1: ",stdout);
	//fputs(echoString,stdout);
	printf("\n");

	// Receive string from server

	unsigned int totalRecvLen = 0;

	//fputs("Client2: ", stdout);

	char buffer[BUFSIZE];
		memset(buffer, 0, BUFSIZE);
		ssize_t recvLen = recv(sockfd, buffer, BUFSIZE - 1, 0);
		if (recvLen < 0) {
			perror("recv() failed");
			exit(-1);
		}
		buffer[recvLen] = '\n';
		
		fputs(buffer, stdout);


	
    // continuation of chat 

    
	
	for(;;){

	char send_buffer[100];
	//fputs("\t \t \tClient1: ",stdout);
	fputs("\t \t \t ",stdout);
	fgets(send_buffer , sizeof(send_buffer),stdin);
	//Create a socket
	int sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (sockfd < 0) {
		perror("socket() failed");
		exit(-1);
	}
	
	// Set the server address
	struct sockaddr_in servAddr;
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	int err = inet_pton(AF_INET, servIP, &servAddr.sin_addr.s_addr);
	if (err <= 0) {
		perror("inet_pton() failed");
		exit(-1);
	}
	servAddr.sin_port = htons(servPort);
	
	// Connect to server
	if (connect(sockfd, (struct sockaddr *) &servAddr, sizeof(servAddr)) < 0) {
		perror("connect() failed");
		exit(-1);
	}
	
	size_t StringLen = strlen(send_buffer);


	
	// Send string to server
	ssize_t sentLen = send(sockfd, send_buffer, StringLen, 0);
	if (sentLen < 0) {
		perror("send() failed");
		exit(-1);
	} else if (sentLen != StringLen) {
		perror("send(): sent unexpected number of bytes");
		exit(-1);
	}


			// Receive string from server
	unsigned int totalRecvLen = 0;

	//fputs("Client2: ", stdout);
	while (totalRecvLen < 100) {
		char buffer[100];
		memset(buffer, 0, BUFSIZE);
		ssize_t recvLen = recv(sockfd, buffer,100, 0);
		if (recvLen < 0) {
			perror("recv() failed");
			exit(-1);
		} else if (recvLen == 0) {
			perror("recv() connection closed prematurely");
			exit(-1);
		}
	
		totalRecvLen += recvLen;
		buffer[recvLen] = '\n';
		//printf("%d\n",recvLen );
		fputs(buffer, stdout);	
	}








	}












	//close(sockfd);
	//exit(0);
}