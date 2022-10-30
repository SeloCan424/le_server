from mimetypes import init
import socket
import string
import threading

class Server:
    def __init__(self, host: string, port: int):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    # Function to handle clients'connections
    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                self.clients.remove(client)
                client.close()
                break

    # Main function to receive the clients connection
    def run(self):
        while True:
            print('Server is running and listening ...')
            client, address = self.server.accept()
            print(f'Connection is established with {str(address)}')
            self.clients.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

server = Server('127.0.0.1', 8001)
server.run()