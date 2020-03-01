import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"


def send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open("upload.txt") as f:
            line = f.readline()
            while line:
                pid, data = line.strip().split(sep=":")
                s.sendto(f"{pid}:{data}".encode(), (UDP_IP, UDP_PORT))
                data, ip = s.recvfrom(BUFFER_SIZE)
                print("Received ack %s from the server" % data.decode())
                line = f.readline()
        s.sendto("FIN".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        while data.decode() != "ACK":
            s.sendto("FIN".encode(), (UDP_IP, UDP_PORT))
            data, ip = s.recvfrom(BUFFER_SIZE)
        print("File upload successfully completed.")
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()


if __name__ == "__main__":
    send()
