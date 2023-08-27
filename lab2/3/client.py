import socket
import threading

def receive_board(server_socket):
    while True:
        try:
            board = server_socket.recv(1024).decode()
            print_board(board)
        except:
            print("Connection closed.")
            break

def print_board(board_str):
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board_str[i]} | {board_str[i+1]} | {board_str[i+2]} |")
        print("-------------")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    
    player_symbol = client.recv(1024).decode()
    print(player_symbol)
    
    receive_thread = threading.Thread(target=receive_board, args=(client,))
    receive_thread.start()
    
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
            
            if "win" in message or "draw" in message:
                client.close()
                break
            
            if "Your turn" in message:
                position = input("Choose a position (1-9): ")
                client.send(position.encode())
        except:
            client.close()
            break

if __name__ == "__main__":
    main()
