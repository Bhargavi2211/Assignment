import socket
s = socket.socket()
host = socket.gethostname()
print("Server will start on host:",host)
port = 2606

s.bind((host, port))
print("Server done binding to host and port successfully")
print("Server is waiting for connection")
s.listen(1)
connection, addr = s.accept()
print(addr, "Has connected to server and online")

while True:
    message = input(str(""))
    message = message.encode()
    connection.send(message)
    print("Message has been sent")
    incoming_message = connection.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client:", incoming_message)
   
