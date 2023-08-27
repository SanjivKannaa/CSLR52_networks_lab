import socket
import threading

clients = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)
print("Server is listening...")

def handle_client(client_socket, client_address):
    clients.append(client_socket)
    print(f"Connection from {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            
            print(f"Received from {client_address}: {message}")
            broadcast(message, client_socket)
        except:
            break
    
    clients.remove(client_socket)
    client_socket.close()
    print(f"Connection closed from {client_address}")

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                client_socket.close()
                clients.remove(client_socket)

def main():
    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
