import socket
import os
from faker import Faker

fake = Faker()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_adress = "./socket_file"

try:
    os.unlink(server_adress)
except FileNotFoundError:
    pass

print("Starting up on {}".format(server_adress))

sock.bind(server_adress)
sock.listen(1)

while True:
    print("Waiting for a connection")
    connection, client_adress =sock.accept()
    try:
        print("connection from", client_adress)

        while True:
            
            data = connection.recv(16)
            data_str = data.decode("utf-8")
            print("Received " + data_str)

            if data:
                response = fake.text()
                connection.sendall(response.encode())

            else:
                print("no deta from ", client_adress)
                break
        
    finally:
        print("Closing current connection")
        connection.close()

