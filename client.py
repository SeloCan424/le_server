import string
import threading
import socket

class Client:
    def __init__(self, host: string, port: int):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.x = 0
        self.y = 0

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                message = dict((x.strip(), int(y.strip()))
                    for x, y in (element.split('-')
                        for element in message.split(', ')))
                print(message)
            except:
                print('Error!')
                self.client.close()
                break

    def send(self):
        old_message = None
        while True:
            message = f"player - 1, x - {self.x}, y - {self.y}"
            if message != old_message:
                self.client.send(message.encode('utf-8'))
            old_message = message

    def run(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()