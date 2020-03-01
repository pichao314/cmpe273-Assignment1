import logging
import socket
import time
import sys

logging.basicConfig(level=logging.INFO,
                    filename='tcp_client_out.txt',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

cid = 'A'
delay = 1
count = 10


def send():
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server
    s.connect((TCP_IP, TCP_PORT))
    for i in range(count):
        s.send(f"{cid}:{MESSAGE}".encode())
        data = s.recv(BUFFER_SIZE)
        print(f"received data:{data.decode()}")
        logging.info(f"received data:{data.decode()}")
        time.sleep(delay)
    s.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong arguments!")
    else:
        cid = sys.argv[1]
        delay = int(sys.argv[2])
        count = int(sys.argv[3])
        send()
