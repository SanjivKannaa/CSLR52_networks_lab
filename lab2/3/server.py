import socket
import threading

def handle_client(client_socket, player_number):
    client_socket.send("Welcome to Tic Tac Toe! Waiting for the other player to join...".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            
            # Broadcast the move to the other player
            other_player = 1 if player_number == 2 else 2
            players[other_player - 1].send(message.encode())
        except:
            break
    
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(2)
    print("Supervising Server is listening...")

    player_number = 1
    while player_number <= 2:
        client_socket, client_address = server_socket.accept()
        print(f"Player {player_number} connected from {client_address}")
        players[player_number - 1] = client_socket

        client_handler = threading.Thread(target=handle_client, args=(client_socket, player_number))
        client_handler.start()

        player_number += 1

    print("Both players are connected. Game starting...")
    
    for player_socket in players:
        player_socket.send("Game starting! You are player 1.".encode())

if __name__ == "__main__":
    players = [None, None]
    main()
