import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 55555))
data = mysock.recv(1024)
mysock.close()
print(data.decode())