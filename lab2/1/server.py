import socket
import re
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def evaluate_expression(expression):
    tokens = re.findall(r'\d+|\S', expression)
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                return "Invalid expression"
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                result = operators[token](op1, op2)
                stack.append(result)
        else:
            return "Invalid expression"
    
    if len(stack) != 1:
        return "Invalid expression"
    
    return stack[0]

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(1)
    
    print("Server is listening...")
    
    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        
        data = conn.recv(1024).decode()
        if not data:
            break
        
        result = evaluate_expression(data)
        conn.send(str(result).encode())
        
        conn.close()

if __name__ == "__main__":
    main()
