import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

player = 1
x = 0
y = 0

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            message = dict((x.strip(), int(y.strip()))
                for x, y in (element.split('-')
                    for element in message.split(', ')))
            print(message)
        except:
            print('Error!')
            client.close()
            break

def client_send():
    #while True:
    message = f"player - {player}, x - {x}, y - {y}"
    client.send(message.encode('utf-8'))

def main():
    receive_thread = threading.Thread(target=client_receive)
    receive_thread.start()

    send_thread = threading.Thread(target=client_send)
    send_thread.start()

if __name__ == '__main__':
    main()