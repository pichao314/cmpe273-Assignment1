# cmpe273-Assignment1
Implement TCP and UDP C/S model

- Run both TCP and UDP and save their output into tcp_sever_out.txt and tcp_clients_out.txt to the tcp folder, and udp_sever_out.txt and udp_client_out.txt to the udp folder.

- Check in all your code and output *.txt files to your private repo named "cmpe273-assignment1".

- Add sithu and ajthakare as collaborator to the assignment 1 repo.

- Submit the assignment 1 repo URL.

# Appendix

## Assignment 1 - Part A

You will be building a simple TCP server that can handle requests from multiple TCP clients. The given baseline implementation does not support handling connection from multiple clients.

### Requirements

* Add handling connection from the multiple clients and the server must be kept running forever.
* Print out the data received by the server along with client id.
* Response all clients to the "pong" message.

### Expected Output

* Starting TCP Server

```
python3 tcp_server.py
Server started at port 5000.
Connected Client:A.
Received data:A:ping
Connected Client:B.
Received data:B:ping
Received data:A:ping
Received data:B:ping
Received data:A:ping
Received data:B:ping
...
```

* Running TCP Clients

_Usage_

```
python3 tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]
```

_Client A_

```
python3 tcp_client.py A 10 3
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
```

_Client B_

```
python3 tcp_client.py B 10 5
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
Sending data:ping
Recevied data:pong
```

## Assignment 1 - Part B

You will be adding package lost detection and reliable message delivery to UDP.

### Requirements

* Implement a simple acknowledgement protocol that you assign unique sequence id for each package you send to the server.
* Once the package is received by the server, the server will send acknowledgement back to the client.
* In case of package lost, the client did not receive the acknowledgement back from the server, the client must resend the same package again until you get the acknowledgement.
* To control the package order, the client will never send the next package until it gets the acknowledegement for the previous one.

### Expected Output

* Starting UDP Server

```
python3 udp_server.py

Server started at port 4000.
Accepting a file upload...
Upload successfully completed.
```

* Running UDP Client

```
python3 udp_client.py

Connected to the server.
Starting a file (upload.txt) upload...
Received ack(xxxxxx) from the server.
Received ack(xxxxxx) from the server.
.
..
File upload successfully completed.
```