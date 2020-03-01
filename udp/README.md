# UDP

## Introduce

This UDP C/S model can handle package lost by setting time out of receiving the last package id.

In order the meet package loss, each time the server will generate a random number list to skip the package receiving
 when the sequence number equals to the number in list.

## Result

We use a simple test file with 20 package to test, from following output we can see that the client will not send
 following package if the previous ACK is not received. The duplicated number in the error list performed the
  situation of long-time loss.

The output of the server:

```shell script
Server started at port 4000
The error id would be [20, 20, 16, 7, 7]
Error id 7
Error id 7
Error id 16
Error id 20
Error id 20
Upload successfully completed.
```

The output of the client:

```shell script
Connected to the server.
Starting a file (test.txt) upload...
Received ack(1) from the server
Received ack(2) from the server
Received ack(3) from the server
Received ack(4) from the server
Received ack(5) from the server
Received ack(6) from the server
The no.7 package was missed!Retrying...
The no.7 package was missed!Retrying...
Received ack(7) from the server
Received ack(8) from the server
Received ack(9) from the server
Received ack(10) from the server
Received ack(11) from the server
Received ack(12) from the server
Received ack(13) from the server
Received ack(14) from the server
Received ack(15) from the server
The no.16 package was missed!Retrying...
Received ack(16) from the server
Received ack(17) from the server
Received ack(18) from the server
Received ack(19) from the server
The no.20 package was missed!Retrying...
The no.20 package was missed!Retrying...
Received ack(20) from the server
File upload successfully completed.
```

# Requirement

## Assignment 1 - Part B

You will be adding package lost detection and reliable message delivery to UDP.

## Requirements

* Implement a simple acknowledgement protocol that you assign unique sequence id for each package you send to the server.
* Once the package is received by the server, the server will send acknowledgement back to the client.
* In case of package lost, the client did not receive the acknowledgement back from the server, the client must resend the same package again until you get the acknowledgement.
* To control the package order, the client will never send the next package until it gets the acknowledegement for the previous one.

## Expected Output

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