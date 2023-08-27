import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
            if "Game over" in message:
                client_socket.close()
                break
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        try:
            move = input("Enter your move (row col): ")
            client_socket.send(move.encode())
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
