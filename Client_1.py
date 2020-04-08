import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter hostname of server:"))
port = 2606

s.connect((host, port))

print("Connect to chat server")
while True:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server:", incoming_message)
    message = input(str(">> "))
    message = message.encode()
    s.send(message)
    print("Message has been sent")
    
