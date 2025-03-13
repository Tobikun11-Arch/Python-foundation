import socket

HOST = "127.0.0.1" 
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    print("Welcome to our shop Assistance! How can I help you today? (Type 'end' to exit)")
    
    while True:
        client_msg = input("Client: ")

        if client_msg.lower() == "end":
            client_socket.send("end".encode())
            break

        client_socket.send(client_msg.encode()) #client send msg to server

        server = client_socket.recv(1024).decode()
        print(f"Server: {server}")

#We use with block so it can automatically closed when the block exits  