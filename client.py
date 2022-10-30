import socket
import threading

my_dict = {'name': "P1", 'x': 0, 'y': 0}

class Client:
    def __init__(self, host, port) -> None:
        # Choosing Nickname
        self.nickname = input("Choose your nickname: ")

        # Connection Data
        self.host = host
        self.port = port

        # Initializing Client
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Receiving Messages From Server
    def receive(self):
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.sendall(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                self.client.close()
                break

    # Sending Messages To Server
    def write(self):
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            self.client.sendall(message.encode('ascii'))

    def run(self):
        # Connecting To Server
        self.client.connect((self.host, self.port))

        # Starting Threads For Listening And Writing
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

def main():
    client = Client('127.0.0.1', 8001)
    client.run()

if __name__ == '__main__':
    main()