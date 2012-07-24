import socket
import sys
from threading import Thread

s = socket.socket()
s.connect (("10.242.11.167", 1234))

def recv():
    while True:
        data = s.recv(1024)
        if not data: sys.exit(0)
        print data

Thread(target=recv).start()

while True:
    data = raw_input('>>>> ')
    if not data: break
    s.send(data)

s.close()