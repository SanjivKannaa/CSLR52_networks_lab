import socket
import threading

class AuctionItem:
    def __init__(self, name, initial_price):
        self.name = name
        self.current_price = initial_price
        self.highest_bidder = None

    def place_bid(self, bidder, bid_amount):
        if bid_amount > self.current_price:
            self.current_price = bid_amount
            self.highest_bidder = bidder
            return True
        return False

    def __str__(self):
        return f"{self.name}: Current Price - {self.current_price}, Highest Bidder - {self.highest_bidder}"

class AuctionServer:
    def __init__(self):
        self.auction_items = {}
        self.lock = threading.Lock()

    def add_item(self, item):
        self.auction_items[item.name] = item

    def handle_client(self, client_socket):
        while True:
            client_socket.send("1. List Auction Items\n2. Bid for an Item\n3. Exit\n".encode())
            choice = client_socket.recv(1024).decode()

            if choice == "1":
                items_list = "\n".join([item.name for item in self.auction_items.values()])
                client_socket.send(items_list.encode())
            elif choice == "2":
                items_list = "\n".join([item.name for item in self.auction_items.values()])
                client_socket.send(items_list.encode())
                item_name = client_socket.recv(1024).decode()
                if item_name in self.auction_items:
                    self.handle_auction(item_name, client_socket)
                else:
                    client_socket.send("Item not found.".encode())
            elif choice == "3":
                client_socket.send("Goodbye!".encode())
                break
            else:
                client_socket.send("Invalid choice. Please select again.".encode())

    def handle_auction(self, item_name, client_socket):
        auction_item = self.auction_items[item_name]
        client_socket.send(f"Auction for '{item_name}' started with initial price: {auction_item.current_price}".encode())
        
        while True:
            client_socket.send("Enter your bid: ".encode())
            bid_amount = int(client_socket.recv(1024).decode())
            if auction_item.place_bid(client_socket.getpeername(), bid_amount):
                client_socket.send(f"Bid accepted! Current highest bid: {auction_item.current_price} by {auction_item.highest_bidder}".encode())
            else:
                client_socket.send("Your bid was not accepted. Please bid a higher amount.".encode())
                break

def main():
    auction_server = AuctionServer()

    item1 = AuctionItem("Painting", 100)
    item2 = AuctionItem("Antique Watch", 200)
    item3 = AuctionItem("Rare Coin", 150)

    auction_server.add_item(item1)
    auction_server.add_item(item2)
    auction_server.add_item(item3)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Auction Server is listening...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Client connected: {client_addr}")
        threading.Thread(target=auction_server.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
