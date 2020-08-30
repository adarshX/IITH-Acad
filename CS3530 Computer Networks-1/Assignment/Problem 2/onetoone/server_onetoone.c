#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define BUFSIZE 1024

static const int MAXPENDING = 5; // Maximum outstanding connection requests

int main(int argc, char ** argv) {

	if (argc != 2) {
		perror("<server port>");
		exit(-1);
	}
	fputs("\t \t \t -----Server's environment------ ",stdout);
	in_port_t servPort = atoi(argv[1]); // Local port

	// create socket for incoming connections
	int servSock;
	if ((servSock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) {
		perror("socket() failed");
		exit(-1);
	}

	// Set local parameters
	struct sockaddr_in servAddr;
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(servPort);

	// Bind to the local address
	if (bind(servSock, (struct sockaddr *) &servAddr, sizeof(servAddr)) < 0) {
		perror("bind() failed");
		exit(-1);
	}

	// Listen to the client
	if (listen(servSock, MAXPENDING) < 0) {
		perror("listen() failed");
		exit(-1);
	}
	int i = 0;
	// Server Loop
	for (;;) {
		struct sockaddr_in clntAddr;
		socklen_t clntAddrLen = sizeof(clntAddr);

		// Wait for a client to connect
		int clntSock = 
				accept(servSock, (struct sockaddr *) &clntAddr, &clntAddrLen);
		if (clntSock < 0) {
			perror("accept() failed");
			exit(-1);
		}

		char clntIpAddr[INET_ADDRSTRLEN];
		if(i == 0){
			
		if (inet_ntop(AF_INET, &clntAddr.sin_addr.s_addr, 
				clntIpAddr, sizeof(clntIpAddr)) != NULL  ) {
			printf("----\nHandling client %s %d\n", 
					clntIpAddr, ntohs(clntAddr.sin_port));
			
		} else {
			puts("----\nUnable to get client IP Address");
		}
	}

		// Receive data
		char buffer[BUFSIZE];
		memset(buffer, 0, BUFSIZE);
		ssize_t recvLen = recv(clntSock, buffer, BUFSIZE - 1, 0);
		if (recvLen < 0) {
			perror("recv() failed");
			exit(-1);
		}
		//buffer[recvLen] = '\n';

		fputs("Client: ", stdout);
		fputs(buffer, stdout);
		if(i == 0)
		{printf("\n");}
		i = i+1;

		//send data

		char send_buffer[BUFSIZE];
		fputs("\t \t \t \t \tServer: ",stdout);
		fgets(send_buffer , sizeof(send_buffer),stdin);
		//scanf("%s",send_buffer);

		ssize_t sentLen = send(clntSock, send_buffer, BUFSIZE - 1, 0);
			if (sentLen < 0) {
				perror("send() failed");
				exit(-1);
			} 
	}

	printf("End of Program\n");

}
