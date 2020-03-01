import logging
import os
import socket
from _thread import *
import threading

logging.basicConfig(level=logging.INFO,
                    filename='tcp_server_out.txt',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:
        data = c.recv(BUFFER_SIZE)
        if not data:
            print('Connection closed.')
            logging.info('Connection closed')
            break
        print(f"received data:{data.decode()}")
        logging.info(f"received data:{data.decode()}")
        c.send("pong".encode())
    c.close()


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print(f'Connection address:{addr}')
        logging.info(f'Connection address:{addr}')
        start_new_thread(threaded, (conn,))

    # s.close()


if __name__ == "__main__":
    os.remove("tcp_client_out.txt")
    # os.remove("tcp_server_out.txt")
    while True:
        listen_forever()
