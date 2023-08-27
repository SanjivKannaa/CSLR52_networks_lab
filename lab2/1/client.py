import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    
    while True:
        expression = input("Enter an expression: ")
        client.send(expression.encode())
        
        result = client.recv(1024).decode()
        print(f"Result: {result}")
    
    client.close()

if __name__ == "__main__":
    main()
