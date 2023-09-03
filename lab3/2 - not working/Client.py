import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        client_socket.send(choice.encode())

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            client_socket.send(username.encode())
            client_socket.send(password.encode())
            response = client_socket.recv(1024).decode()
            print(response)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            client_socket.send(username.encode())
            client_socket.send(password.encode())
            response = client_socket.recv(1024).decode()
            print(response)
            if response == "Login successful":
                while True:
                    print("1. Store Data\n2. Retrieve Data\n3. Logout")
                    action = input("Enter your action: ")
                    client_socket.send(action.encode())
                    if action == "1":
                        key = input("Enter key: ")
                        value = input("Enter value: ")
                        client_socket.send(key.encode())
                        client_socket.send(value.encode())
                        response = client_socket.recv(1024).decode()
                        print(response)
                    elif action == "2":
                        key = input("Enter key: ")
                        client_socket.send(key.encode())
                        value = client_socket.recv(1024).decode()
                        print(f"Value: {value}")
                    elif action == "3":
                        break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

    client_socket.close()

if __name__ == "__main__":
    main()
