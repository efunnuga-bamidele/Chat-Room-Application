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


def handle_clients(conn, address):
    connected_client_name = conn.recv(1024).decode()
    greeting = f"Welcome {connected_client_name}. You can type #quit if you ever wannt to leave the Chat Room"
    conn.recv(bytes(greeting, "utf8"))
    msg = f"{connected_client_name} has recently joined the Chat Room"
    broadcast(bytes(msg, "utf8"))
    clients_connected[conn] = connected_client_name

    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, connected_client_name+":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients_connected[conn]
            broadcast(bytes(f"{connected_client_name} has left the Chat Room"))


def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, "Has connected!")
        client_conn.send((" Welcome to the Chat Room, Please Type your name to continue".encode('utf8')))
        clients_addresses[client_conn] = client_address

        Thread(target=handle_clients, args=(client_conn, client_address)).start()


def broadcast(msg, prefix=""):
    for client in clients_connected:
        client.send(bytes(prefix, "utf8") +msg)


if __name__ == "__main__":
    sock.listen(6)
    print("The Server is running and is listening to clients requests")

    thread_one = Thread(target=accept_client_connections)
    thread_one.start()
    thread_one.join()
