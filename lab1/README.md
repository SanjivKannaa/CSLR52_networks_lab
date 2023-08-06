#NETWORKS LAB QN, 7AUG2023

a)Create three programs, two of which are clients to a single server. Client1 will send a character to the server process. The server will decrement the letter to the next letter in the alphabet and send the result to client2. Client2 prints the letter it receives and then all the processes terminate.

b)Write a socket program to enable client1 to send a float value to the server. The server process should increase the value of the number it receives by a power of 1.5. The server should print both the value it receives and the value that it sends. Client2 should print the value it receives from the server.

c)Send datagrams with two arrays of integers (only even numbers) to a server. The server should check the data, whether there are odd and/or fraction numbers. If it is not, the server sums the elements of each array and puts the sum in a third array that is returned to the client. If the server discovers that the arrays have erroneous then the server does not reply. A timeout period should be established by the client such that retransmission occurs after the period expires. 

d)Implement a port scanner using socket programming. The port scanner checks a number of ports (for instance, from 1 to 1026) to see if they are open (a server is listening on that port number) or closed (a server is not listening on that port number)