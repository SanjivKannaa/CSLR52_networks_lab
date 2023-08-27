import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                remove_client(client_socket)
                break
            
            broadcast(message, client_socket)
        except:
            remove_client(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                continue

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    
    print("Server is listening...")
    
    while True:
        client_socket, client_addr = server.accept()
        clients.append(client_socket)
        
        print(f"Connected to {client_addr}")
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
