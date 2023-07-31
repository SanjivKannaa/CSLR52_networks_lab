import socket


ip = "localhost" # socket.gethostname()#192.168.1.11
port = 8080
client = socket.socket()
client.connect((ip, port))
message = "hello world!"
client.send(message.encode())
client.close()
