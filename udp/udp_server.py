import logging
import socket
import random

logging.basicConfig(level=logging.INFO,
                    filename="udp_server_out.txt",
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

# manually add error id
err = [random.randint(1, 10000) for _ in range(20)]
err.sort(reverse=True)


def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print(f"Server started at port {UDP_PORT}")
    logging.info(f"Server started at port {UDP_PORT}")
    print(f"The error id would be {str(err)}")
    logging.info(f"The error id would be {str(err)}")
    print("Accepting a file upload...")
    logging.info("Accepting a file upload...")

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        while data.decode() != "FIN":
            # reply back to the client
            pid = data.decode(encoding="utf-8").strip().split(sep=":")[0]
            if err and int(pid) == err[-1]:
                eid = err.pop()
                print("Error id %d" % eid)
                logging.info("Error id %d" % eid)
                data, ip = s.recvfrom(BUFFER_SIZE)
                continue
            s.sendto(data.decode(encoding="utf-8").strip().split(sep=":")[0].encode(), ip)
            data, ip = s.recvfrom(BUFFER_SIZE)
        s.sendto("ACK".encode(), ip)
        print("Upload successfully completed.")
        logging.info("Upload successfully completed.")
        break


if __name__ == "__main__":
    listen_forever()
