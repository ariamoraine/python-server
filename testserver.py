import socket
import sys
from threading import Thread

running = True
clientsockets = []

def server_main_loop():
    serversocket = socket.socket()
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serversocket.bind(('10.242.11.167', 5674))
    serversocket.listen(5)
    try:
        while True:
            c = serversocket.accept()
            s = c[0]
            clientsockets.append(s)
            print 'clientsocketlist', clientsockets
            Thread(target=recv, args=(s,)).start()
    except KeyboardInterrupt:
        running = False
        sys.exit()

def client_main_loop():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('10.242.11.167', 5674))
    Thread(target=client_recv, args=(s,)).start()

    while True:
        text = raw_input('>>>> ')
        if running == False:
            sys.exit()
        elif text == 'exit':
            s.send(text)
            s.close()
            sys.exit()
        else:
            print "sending text"
            s.send(text)

def client_recv(s):
    print "starting client"
    global running
    while True:
        try:
            text = s.recv(1024)
            print text
        except socket.error:
            running = False
            s.close()
            sys.exit()


def recv(s):
    print "thread started"
    global running
    while True:
        try:
            data = s.recv(1024)
            print "got some data"
            for sock in clientsockets:
                print "sent some data"
                sock.send(data)
        except socket.error:
            running = False
            sys.exit()
        if data == 'exit':
            running = False
            s.close()
            sys.exit()


if __name__ == '__main__':


    if 'server' in sys.argv:
        server_main_loop()

    else:
        client_main_loop()