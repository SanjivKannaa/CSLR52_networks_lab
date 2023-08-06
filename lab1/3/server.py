import socket

def function(data):
    arr1 = []
    arr2 = []
    flag = False
    for i in data:
        if i=="|":
            flag = True
        elif not flag:
            if i != " ":
                arr1.append(int(i))
        else:
            if i != " ":
                arr2.append(int(i))
    for i in arr1:
        if int(i)!=i or i%2!=0:
            return ""
    for i in arr2:
        if int(i)!=i or i%2!=0:
            return ""
    if len(arr1)!=len(arr2):
        return ""
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return str(result)


ip = "localhost"
port = 8080
server = socket.socket()
server.bind((ip, port))
server.listen()
connection, address = server.accept()
data = connection.recv(1024).decode()
data = function(data)
if (data!=""):
    connection.send(data.encode())
connection.close()