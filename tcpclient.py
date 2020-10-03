#!/usr/bin/python
from socket import *
import threading
import sys


class clientThread(threading.Thread):
    def __init__(self, connectionSocket, clientName):
        threading.Thread.__init__(self)
        self.cname = clientName
        self.socket = connectionSocket

    def run(self):
        # arr.append(self.socket)
        while True:
            sentence = input('You: ')
            res = self.cname + ": " + sentence
            self.socket.send(res.encode())


if (len(sys.argv) < 3):
    sys.exit("Usage: python client.py <port-no> <username>")

serverName = '127.0.0.1'
serverPort = int(sys.argv[1])
clientName = sys.argv[2]
#This is the username of the client

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('\n-----------Welcome to the Chatroom-----------\n')

while True:
    thread = clientThread(clientSocket, clientName)
    thread.daemon = True
    #Die when main thread dies
    thread.start()

    try:
        sentence = clientSocket.recv(1024).decode()
        print("\r" + sentence + "\nYou: ", end='')
        #/r - carriage return - moves cursor to start of line
    except:
        # When a client exits from the chatroom(by Ctrl-C)
        print("\rGoodbye " + clientName)
        break
clientSocket.close()#!/usr/bin/python
from socket import *
import threading
import sys


class clientThread(threading.Thread):
    def __init__(self, connectionSocket, clientName):
        threading.Thread.__init__(self)
        self.cname = clientName
        self.socket = connectionSocket

    def run(self):
        # arr.append(self.socket)
        while True:
            sentence = input('You: ')
            res = self.cname + ": " + sentence
            self.socket.send(res.encode())


if (len(sys.argv) < 3):
    sys.exit("Usage: python client.py <port-no> <username>")

serverName = '127.0.0.1'
serverPort = int(sys.argv[1])
clientName = sys.argv[2]
#This is the username of the client

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('\n-----------Welcome to the Chatroom-----------\n')

while True:
    thread = clientThread(clientSocket, clientName)
    thread.daemon = True
    #Die when main thread dies
    thread.start()

    try:
        sentence = clientSocket.recv(1024).decode()
        print("\r" + sentence + "\nYou: ", end='')
        #/r - carriage return - moves cursor to start of line
    except:
        # When a client exits from the chatroom(by Ctrl-C)
        print("\rGoodbye " + clientName)
        break
clientSocket.close()
