import socket


ip = "localhost" # socket.gethostname()#192.168.1.11
port = 8081
client = socket.socket()
client.connect((ip, port))
data = client.recv(1024).decode()
print("message from server: " + data)
client.close()
