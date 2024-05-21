import socket
import threading

# Function to send messages to the server
def send_message(client_socket):
    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8888))

# Start a thread for sending messages to the server
send_thread = threading.Thread(target=send_message, args=(client,))
send_thread.start()

# Receive messages from the server
while True:
    message = client.recv(1024).decode()
    print(f"Received from server: {message}")