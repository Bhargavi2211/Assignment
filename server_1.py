import socket
import sys
import time
s = socket.socket()
host = socket.gethostname()
print("Server will start on host:",host)
port = 2606

s.bind((host, port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for connection")
print("")
s.listen(5)
conn, add = s.accept()
print(add, "Has connected to server and online")
print("")
while True:
    message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    print("Message has been sent")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client:", incoming_message)
    print("")
