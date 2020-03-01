import logging
import socket

logging.basicConfig(level=logging.INFO,
                    filename="udp_client_out.txt",
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
FILE_NAME = "upload.txt"


def send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server.")
        logging.info("Connected to the server.")
        # read the upload file
        with open(FILE_NAME) as f:
            print("Starting a file (%s) upload..." % FILE_NAME)
            logging.info("Starting a file (%s) upload..." % FILE_NAME)
            # read each line as package
            line = f.readline()
            while line:
                # get the package id and content
                pid, data = line.strip().split(sep=":")
                while True:
                    # send a package a wait for ACK of the package id from server in preset time limit
                    try:
                        s.sendto(f"{pid}:{data}".encode(), (UDP_IP, UDP_PORT))
                        # set the time out
                        s.settimeout(1)
                        data, ip = s.recvfrom(BUFFER_SIZE)
                        # successfully received ack
                        print("Received ack(%s) from the server" % data.decode())
                        logging.info("Received ack(%s) from the server" % data.decode())
                        # check if the id is correct
                        if data.decode() != pid:
                            continue
                        else:
                            break
                    # handle the timeout
                    except socket.timeout:
                        print("The no.%s package was missed!Retrying..." % pid)
                        logging.info("The no.%s package was missed!Retrying..." % pid)
                        # send the package again
                        continue
                line = f.readline()
        # finished uploading, send signal to end
        s.sendto("FIN".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        # KEEP sending signal for ACK from sserver
        while data.decode() != "ACK":
            s.sendto("FIN".encode(), (UDP_IP, UDP_PORT))
            data, ip = s.recvfrom(BUFFER_SIZE)
        # end the session
        print("File upload successfully completed.")
        logging.info("File upload successfully completed.")
        s.close()
    except socket.error:
        print("Error! {}".format(socket.error))
        logging.info("Error! {}".format(socket.error))
        exit()


if __name__ == "__main__":
    send()
