#!/usr/bin/python
from socket import *
import threading
import sys

clientList = []


class serverThread(threading.Thread):
    def __init__(self, addr, connectionSocket):
        threading.Thread.__init__(self)
        self.socket = connectionSocket
        clientList.append(connectionSocket)
        print("New client has joined\n")

    def run(self):
        while True:
            sentence = self.socket.recv(1024).decode()
            for i in clientList:
                try:
                    #send the message to all clients except the sender himself
                    if (i != self.socket):
                        i.send(sentence.encode())
                except:
                    if (i in clientList):
                        clientList.remove(i)
                    # When a client leaves the chat
                    print("Client left\n")


if (len(sys.argv) < 2):
    sys.exit("Usage: python server.py <port-no>")

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

print('\n-----------Welcome to the Server-----------\n')
while True:
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    print('New request received from' + str(addr))

    thread = serverThread(addr, connectionSocket)
    thread.daemon = True
    #Die when main thread dies
    thread.start()
connectionSocket.close()
