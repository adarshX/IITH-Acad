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



	int N; //no .of clients

	//fputs("No.of Clients :");
	//scanf("%d",&N);





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
		//client 1
		struct sockaddr_in clntAddr;
		socklen_t clntAddrLen = sizeof(clntAddr);

		//client2
		struct sockaddr_in clntAddr1;
		socklen_t clntAddrLen1 = sizeof(clntAddr1);

		// Wait for a client1 to connect
		int clntSock = 
				accept(servSock, (struct sockaddr *) &clntAddr, &clntAddrLen);
		if (clntSock < 0) {
			perror("accept() failed");
			exit(-1);
		}

		// Wait for a client2 to connect
		int clntSock1 = 
				accept(servSock, (struct sockaddr *) &clntAddr1, &clntAddrLen1);
		if (clntSock1 < 0) {
			perror("accept() failed");
			exit(-1);
		}

		//client1
		char clntIpAddr[INET_ADDRSTRLEN];
		
			
		if (inet_ntop(AF_INET, &clntAddr.sin_addr.s_addr, 
				clntIpAddr, sizeof(clntIpAddr)) != NULL  ) {
			printf("----\nHandling client %s %d\n", 
					clntIpAddr, ntohs(clntAddr.sin_port));
			
		} else {
			puts("----\nUnable to get client IP Address");
		}
     

     	//client2
		char clntIpAddr1[INET_ADDRSTRLEN];
		
			
		if (inet_ntop(AF_INET, &clntAddr1.sin_addr.s_addr, 
				clntIpAddr, sizeof(clntIpAddr1)) != NULL  ) {
			printf("----\nHandling client %s %d\n", 
					clntIpAddr1, ntohs(clntAddr1.sin_port));
			
		} else {
			puts("----\nUnable to get client IP Address");
		}
	    


		// Receive data from client 1 
		char buffer[BUFSIZE];
		memset(buffer, 0, BUFSIZE);
		ssize_t recvLen = recv(clntSock, buffer, BUFSIZE - 1, 0);
		if (recvLen < 0) {
			perror("recv() failed");
			exit(-1);
		}
		//buffer[recvLen] = '\n';


		fputs("Client1: ", stdout);
		fputs(buffer, stdout);
		//if(i == 0)
		//{printf("\n");}
		//i = i+1;


		//send data from client 1 to client 2

		ssize_t sentLen_12 = send(clntSock1, buffer, BUFSIZE - 1, 0);
			if (sentLen_12 < 0) {
				perror("send() failed");
				exit(-1);
			}



			/*char send_buffer[BUFSIZE];
			fputs("\t \t \t \t \tServer: ",stdout);
			fgets(send_buffer , sizeof(send_buffer),stdin);
			//scanf("%s",send_buffer);
			*/
		/*char  send_buffer1[BUFSIZE];
		send_buffer1 = strcat("Client1",buffer);

		char  send_buffer2[BUFSIZE];
		send_buffer2= strcat("Client2",buffer1);*/
		
		 







		// Receive data from client 2 
		char buffer1[BUFSIZE];
		memset(buffer1, 0, BUFSIZE);
		ssize_t recvLen1 = recv(clntSock1, buffer1, BUFSIZE - 1, 0);
		if (recvLen1 < 0) {
			perror("recv() failed");
			exit(-1);
		}
		//buffer[recvLen] = '\n';


		fputs("Client2: ", stdout);
		fputs(buffer1, stdout);
		//if(i == 0)
		//{printf("\n");}
		//i = i+1;


		
		//send data from client 2 to client 1

			

		ssize_t sentLen_21 = send(clntSock, buffer1, BUFSIZE - 1, 0);
			if (sentLen_21 < 0) {
				perror("send() failed");
				exit(-1);
			} 




	}

	



}