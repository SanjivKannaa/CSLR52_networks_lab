import socket


ip = "localhost" # socket.gethostname()#192.168.1.11
port = 8080
client = socket.socket()
client.connect((ip, port))
while True:
    print("enter the message [q to quit]: ", end='')
    message = input()
    if message == "q":
        client.send("".encode())
        break
    client.send(message.encode())
client.close()
