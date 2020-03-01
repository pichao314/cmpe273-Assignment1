import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print(f"Server started at port {UDP_PORT}")

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        while data.decode() != "FIN":
            # reply back to the client
            s.sendto(data.decode(encoding="utf-8").strip().split(sep=":")[0].encode(), ip)
            data, ip = s.recvfrom(BUFFER_SIZE)
        s.sendto("ACK".encode(), ip)
        print("Upload successfully completed.")
        break


if __name__ == "__main__":
    listen_forever()
