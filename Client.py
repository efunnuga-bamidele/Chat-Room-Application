import socket

host_address = 'localhost'
host_port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host_address, host_port))

message = sock.recv(1024)

while message:
    print(f"Message: {message.decode()}")
    message = sock.recv(1024)

sock.close()