import socket


ip = "localhost" # socket.gethostname()#192.168.1.11
result = []

client = socket.socket()
for port in range(int(input("starting port: ")), int(input("ending port: "))+1):
    try:
        client.connect((ip, port))
        client.close()
        result.append(port)
    except:
        pass
print("open ports: " + str(result))