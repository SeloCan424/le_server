import socket
import threading

HEADER = 64
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        data_lenght = conn.recv(HEADER).decode(FORMAT)
        if data_lenght:
            data_lenght = int(data_lenght)
            data = conn.recv(data_lenght).decode(FORMAT)

            if data == DISCONNECT_MESSAGE:
                connected = False
    
            print(f"[{addr}] {data}")
            for client in clients:
                client.send(data.encode(FORMAT))
    conn.close()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

def main():
    print("[STARTING] Server is starting ...")
    s.listen()
    print(f"[LISTENING] The server is listening on {HOST}")
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        

if __name__ == '__main__':
    main()