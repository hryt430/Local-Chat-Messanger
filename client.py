import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_adress = "/socket_file"
print("connecting to {}".format(server_adress))

try:
    sock.connect(server_adress)
except sock.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        message = input("Type the message you wanna send to the server side: ").encode()
        if message:
            sock.sendall(message)

            sock.timeout(2)

            try:
                while True:
                    data = str(sock.recv(32))

                    if data:
                        print("Server response " + data)
                    else:
                        break
            
            except TimeoutError:
                print("Socket timeout, ending listenig for server message")
        else:
            print("no deta to send to the server side")
            break
finally:
    print("Closing socket")
    sock.close()

