import socket
from threading import Thread

host_address = '127.0.0.1'
host_port = 8080

clients_connected = {}
clients_addresses = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host_address, host_port))

# sock.listen(1)
# print("The Server is running and is listening to client request")
# conn, address = sock.accept()
#
# message = "Hey there is something important for you"
# conn.send(message.encode())
#
# conn.close()


def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, "Has connected!")
        client_conn.send((" Welcome to the Chat Room, Please Type your name to continue".encode('utf8')))
        clients_addresses[client_conn] = client_address


if __name__ == "__main__":
    sock.listen(6)
    print("The Server is running and is listening to clients requests")

    thread_one = Thread(target = accept_client_connections)
    thread_one.start()
    thread_one.join()