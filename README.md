A TCP client-server application that implements a chat server, using multi-threading.

The programs run like this:

$ python server.py <port-no> # and now server is running 

$ python client.py <port-no> <username>

Where <username> will be shown as your name for chatting.

While <port-no> is the port number to which the server binds itself.

The server will create a single "broadcast" chatroom for the computer and everyone connecting to the server will be able to see everyone else's messages.# TCP-client-server-Chat-Application
