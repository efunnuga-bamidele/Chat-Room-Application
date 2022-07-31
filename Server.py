import socket

host_address = 'localhost'
host_port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host_address, host_port))

sock.listen(1)
print("The Server is running and is listening to client request")
conn, address = sock.accept()

message = "Hey there is something important for you"
conn.send(message.encode())

conn.close()