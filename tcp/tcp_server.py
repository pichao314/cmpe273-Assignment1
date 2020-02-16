import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024


def listen_forever():
    # create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to the port
    s.bind((TCP_IP, TCP_PORT))
    # listen for incoming connections
    s.listen(1)

    while True:
        # Wait for a connection
        print("Waiting for a connection")
        conn, addr = s.accept()
        try:
            print(f'Connection address:{addr}')

            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    print("No data received.")
                    break
                # print(data.decode().split(':'))
                id, msg = data.decode().split(':')
                if id=='0':
                    break
                print("received data from client %s:%s" % (id, msg))
                conn.send("pong".encode())
        finally:
            conn.close()
        break


if __name__ == "__main__":
    listen_forever()

#     conn, addr = s.accept()
#     print(f'Connection address:{addr}')

#     while True:
#         data = conn.recv(BUFFER_SIZE)
#         if not data:
#             print('No data received.')
#             break
#         print(f"received data:{data.decode()}")
#         conn.send("pong".encode())

#     conn.close()


# listen_forever()
