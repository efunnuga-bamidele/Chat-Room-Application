import socket
import tkinter
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("There was an error while receiving the message")


def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        window.close()


def on_closing():
    my_msg.set("#quit")
    send()


window = Tk()
window.title("Chat Room App")
window.configure(bg="gray")

message_frame = Frame(window, height=100, width=100, bg="red")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="red", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg="blue", font="Ariel", bg="white")
label.pack()

entry_field = Entry(window, textvariable=my_msg, fg="red", width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Ariel", fg="black", command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font="Ariel", fg="black", command=on_closing)
quit_button.pack()

host_address = '127.0.0.1'
host_port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host_address, host_port))

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()

#

#
# message = sock.recv(1024)
#
# while message:
#     print(f"Message: {message.decode()}")
#     message = sock.recv(1024)
#
# sock.close()
