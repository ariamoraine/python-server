import socket
import sys
from threading import Thread

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect (("10.242.11.167", 5674))

def recv():
    while True:
        data = s.recv(1024)
        # x = '2'
        print data
        if data == 'new':
            print "it worked"
            s.close()
            sys.exit()
        # s.close()
        # if not data: break

Thread(target=recv).start()

while True:
    text = raw_input('>>>> ')
    # c = '1'
    s.send(text)
    if text == 'new':
        s.close()
        sys.exit()
    
    # s.close()
    # if not text: break

s.close()