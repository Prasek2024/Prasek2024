import socket
import threading


# Function to handle client messages
def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection with {client_address} closed.")
            break
        print(f"Received message from {client_address}: {message}")


# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("Server is listening for incoming connections...")

# Accept incoming connections and start a new thread for each client
while True:
    client_socket, client_address = server.accept()
    print(f"Connection established with {client_address}")

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()