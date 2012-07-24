import socket
from threading import Thread

s = socket.socket()
s.bind(('10.242.11.167', 1234))

s.listen(5)
c = s.accept()
s = c[0]
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