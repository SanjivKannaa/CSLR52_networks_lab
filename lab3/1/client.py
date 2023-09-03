import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("1. List Auction Items\n2. Bid for an Item\n3. Exit")
        choice = input("Enter your choice: ")
        client_socket.send(choice.encode())

        if choice == "1":
            items_list = client_socket.recv(1024).decode()
            print("Auction Items:")
            print(items_list)
        elif choice == "2":
            items_list = client_socket.recv(1024).decode()
            print("Auction Items:")
            print(items_list)
            item_name = input("Enter the name of the item for auction: ")
            client_socket.send(item_name.encode())
            response = client_socket.recv(1024).decode()
            print(response)
            if "started" in response:
                while True:
                    bid_amount = int(input("Enter your bid amount: "))
                    client_socket.send(str(bid_amount).encode())
                    response = client_socket.recv(1024).decode()
                    print(response)
                    if "accepted" not in response:
                        break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

    client_socket.close()

if __name__ == "__main__":
    main()
