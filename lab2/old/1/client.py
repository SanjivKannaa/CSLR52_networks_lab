import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        expression = input("Enter an infix expression: ")
        client_socket.send(expression.encode())

        result = client_socket.recv(1024).decode()
        print("Result:", result)

        choice = input("Do you want to enter another expression? (y/n): ")
        if choice.lower() != 'y':
            break

    client_socket.close()

if __name__ == "__main__":
    main()
