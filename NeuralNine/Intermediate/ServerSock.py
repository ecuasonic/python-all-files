# A socket is just the end point of a communication channel
#     When you have a communication in a network, you always have two end points, and these endpoints are called sockets
#     Serve and a client, or two clients
#     Two sockets trying to exchange data
# If dealing with sockets, we are dealing with the lower levels of connectivity 
#     Connection-oriented protocal TCP and connectionless protocal UDP
#     TCP is better for any sensible data (data to be sent and to be recieved), but slower than UDP
#     UDP, you have the risk to losing data, but way faster (video games or skype calls)
# If you want to use higher-level, you would have to use the actual applications, such as FTP, HTTP, and different python modules

import socket
# Internet or UNIX socket?
# TCP or UDP socket?
# Connection and host IP choice?
# Port choice?

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP is SOCK_STREAM while UDP is SOCK_DGRAM
mysock.bind(('127.0.0.1',55555)) # This is the host and port of the socket we want to run on 
mysock.listen() # makes the socket as a host server and listens for clients attempting to connect

while True:
    client, address = mysock.accept() # When clients want to connect to the server/socket and we accept them 
    print(f"Connected to {client} {address}")
    client.send("You are connected!".encode())
    client.close() # closes the client to prevent unlimited clients running in the background