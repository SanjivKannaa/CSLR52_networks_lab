import socket
import re
import operator

def evaluate_expression(expression):
    # Tokenize the expression
    tokens = re.findall(r'\d+|\+|-|\*|/', expression)
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            result = operators[token](op1, op2)
            stack.append(result)

    return stack[0]

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on", host, "port", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from", client_address)

        data = client_socket.recv(1024).decode()
        if not data:
            break

        result = evaluate_expression(data)
        client_socket.send(str(result).encode())

        client_socket.close()

if __name__ == "__main__":
    main()
