import socket

HOST = "127.0.0.1"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        Client_message = conn.recv(1024).decode()
        print("Client: ", Client_message)

        if Client_message.lower() == "end":
            print("Client ended the chat. Server shutting down.")
            break

        response = input("Server: ")
        conn.send(response.encode())