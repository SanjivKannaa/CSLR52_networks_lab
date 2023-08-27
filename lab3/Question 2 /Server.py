import socket
import threading
import hashlib

class AuthService:
    def __init__(self):
        self.users = {}  # User data: username -> password_hash
        self.data = {}   # Data storage: username -> {key -> value}

    def signup(self, username, password):
        if username in self.users:
            return "Username already exists"
        self.users[username] = hashlib.sha256(password.encode()).hexdigest()
        self.data[username] = {}
        return "Signup successful"

    def login(self, username, password):
        if username in self.users and self.users[username] == hashlib.sha256(password.encode()).hexdigest():
            return "Login successful"
        return "Invalid credentials"

    def store_data(self, username, key, value):
        if username in self.data:
            self.data[username][key] = value
            return "Data stored successfully"
        return "User not found"

    def retrieve_data(self, username, key):
        if username in self.data and key in self.data[username]:
            return self.data[username][key]
        return "Data not found"

def handle_client(client_socket):
    auth_service = AuthService()

    while True:
        client_socket.send("1. Signup\n2. Login\n3. Exit\n".encode())
        choice = client_socket.recv(1024).decode()

        if choice == "1":
            username = client_socket.recv(1024).decode()
            password = client_socket.recv(1024).decode()
            response = auth_service.signup(username, password)
            client_socket.send(response.encode())
        elif choice == "2":
            username = client_socket.recv(1024).decode()
            password = client_socket.recv(1024).decode()
            response = auth_service.login(username, password)
            client_socket.send(response.encode())
            if response == "Login successful":
                while True:
                    client_socket.send("1. Store Data\n2. Retrieve Data\n3. Logout\n".encode())
                    action = client_socket.recv(1024).decode()
                    if action == "1":
                        key = client_socket.recv(1024).decode()
                        value = client_socket.recv(1024).decode()
                        response = auth_service.store_data(username, key, value)
                        client_socket.send(response.encode())
                    elif action == "2":
                        key = client_socket.recv(1024).decode()
                        value = auth_service.retrieve_data(username, key)
                        client_socket.send(value.encode())
                    elif action == "3":
                        break
        elif choice == "3":
            client_socket.send("Goodbye!".encode())
            break
        else:
            client_socket.send("Invalid choice. Please select again.".encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Auth Service is listening...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Client connected: {client_addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
