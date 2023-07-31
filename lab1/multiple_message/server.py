import socket


ip = "localhost" #socket.gethostname()#192.168.1.11
port = 8080
server = socket.socket()
server.bind((ip, port))
server.listen()
connection, address = server.accept()
print("connected to client: ", address[0])
while True:
    data = connection.recv(1024).decode()
    if (data==""):
        print("client disconnected...")
        break
    print(address[0] + ": " + data)
connection.close()
