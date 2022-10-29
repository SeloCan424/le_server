import socket

HEADER = 64
HOST = "192.168.188.38"
PORT = 8000
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)

def main():
    client.connect(ADDR)
    send(input())
    while True:
        data = client.recv(HEADER).decode(FORMAT)
        print(data)

if __name__ == '__main__':
    main()