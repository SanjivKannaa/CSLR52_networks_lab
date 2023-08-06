import socket

ip = "localhost"
port = 8080

client = socket.socket()
client.connect((ip, port))
arr1 = input("enter the first array(seperated by space \" \"): ")
arr2 = input("enter the second array(seperated by space \" \"): ")
data = arr1 + "|" + arr2
client.send(data.encode())
data = client.recv(1024).decode()
print(data)
client.close()