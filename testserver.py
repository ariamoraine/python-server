import socket
import sys
from threading import Thread

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
running = True

if 'server' in sys.argv:
    s.bind(('10.242.11.167', 5674))
    s.listen(5)
    c = s.accept()
    s = c[0]
else:
    s.connect(('10.242.11.167', 5674))

def recv():
    global running
    while True:
        try:
            data = s.recv(1024)
            print data
        except socket.error:
            sys.exit()
        if data == 'exit':
            running = False
            s.close()
            sys.exit()


Thread(target=recv).start()

while True:
    text = raw_input('>>>> ')
    if running == False:
        sys.exit()
    elif text == 'exit':
        s.send(text)
        s.close()
        sys.exit()
    else:
        s.send(text)
