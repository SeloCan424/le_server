import socket
import threading

class Server:
    def __init__(self, host, port):
        # Initializing Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connection Data
        self.host = host
        self.port = port

        # Lists For Clients and Their Nicknames
        self.clients = []
        self.nicknames = []

    # Sending Messages To All Connected Clients
    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    # Handling Messages From Clients
    def handle(self, client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)
                self.broadcast(message)
            except:
                # Removing And Closing Clients
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast('{} left!'.format(nickname).encode('ascii'))
                self.nicknames.remove(nickname)
                break

    # Receiving / Listening Function
    def run(self):
        # Starting Server
        self.server.bind((self.host, self.port))
        self.server.listen()
        while True:
            # Accept Connection
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            self.broadcast("{} joined!".format(nickname).encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

def main():
    server = Server('127.0.0.1', 8001)
    server.run()

if __name__ == '__main__':
    main()