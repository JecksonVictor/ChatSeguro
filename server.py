from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
import sys

connected = False

# __main__
socket = socket(AF_INET, SOCK_STREAM)

def waitConnect(socket, port=int(sys.argv[1])):
    socket.bind(('', port))
    socket.listen(1)

    con, client = socket.accept()
    print(client, " connected.")
    
    connected = True

def getMessage():
    while connected:
        print(str(socket.recv(1024), 'utf-8'))

def sendMessage():
    while connected:
        message = input()
        socket.send(str.encode(message))

#Espera
Thread(target=waitConnect, args=()).start()

while connected == False:
    pass

#Aguarda mensagens
Thread(target=getMessage, args=()).start()

#Envia
Thread(target=sendMessage, args=()).start()