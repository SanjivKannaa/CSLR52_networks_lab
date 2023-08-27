import socket
import threading

# Tic Tac Toe board
board = [" " for _ in range(9)]
current_player = "X"

def send_board(player_socket):
    player_socket.send("".join(board).encode())

def handle_player(player_socket, player_symbol):
    global current_player
    
    while True:
        try:
            send_board(player_socket)
            
            if current_player == player_symbol:
                player_socket.send("Your turn. Choose a position (1-9): ".encode())
                position = int(player_socket.recv(1024).decode()) - 1
                
                if board[position] == " ":
                    board[position] = player_symbol
                    current_player = "O" if player_symbol == "X" else "X"
                else:
                    player_socket.send("Invalid move. Try again.".encode())
            else:
                player_socket.send("Waiting for the opponent's move...".encode())
            
            # Check for a win or draw
            winner = check_winner()
            if winner:
                send_board(player_socket)
                player_socket.send(f"Player {player_symbol} wins!".encode())
                break
            elif " " not in board:
                send_board(player_socket)
                player_socket.send("It's a draw!".encode())
                break
        except:
            break
    
    player_socket.close()

def check_winner():
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    
    for pos1, pos2, pos3 in winning_positions:
        if board[pos1] == board[pos2] == board[pos3] != " ":
            return board[pos1]
    return None

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(2)
    
    print("Server is listening...")
    
    player_sockets = []
    
    for _ in range(2):
        player_socket, _ = server.accept()
        player_sockets.append(player_socket)
        
        player_symbol = "X" if len(player_sockets) == 1 else "O"
        player_socket.send(f"You are Player {player_symbol}".encode())
        
        player_thread = threading.Thread(target=handle_player, args=(player_socket, player_symbol))
        player_thread.start()

if __name__ == "__main__":
    main()
