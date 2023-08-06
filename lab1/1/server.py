import socket


ip = "localhost" #socket.gethostname()#192.168.1.11
port = 8080
server = socket.socket()
server.bind((ip, port))
server.listen()
connection, address = server.accept()
print("connected to client1: ", address[0])
data = connection.recv(1024).decode()
connection.close()

ip = "localhost" #socket.gethostname()#192.168.1.11
port = 8081
server = socket.socket()
server.bind((ip, port))
server.listen()
connection, address = server.accept()
print("connected to client2: ", address[0])
# data = connection.recv(1024).decode()
data = chr(ord(data)+1)
connection.send(data.encode())
connection.close()

