from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
import sys

connected = False
socket = socket(AF_INET, SOCK_STREAM)

def getMessage(host, port):
    socket.connect((host, port))
    connected = True
    while connected:
        print(str(socket.recv(1024), 'utf-8'))

def sendMessage():
    while connected:
        message = input()
        socket.send(str.encode(message))

# __ main __
serverIP = (str(sys.argv[1]))
sysPort = (int(sys.argv[2]))

Thread(target=getMessage, args=(serverIP, sysPort)).start()
# send
while connected == False:
    pass

Thread(target=sendMessage, args=()).start()