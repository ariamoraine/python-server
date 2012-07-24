import socket

s = socket.socket()
s.bind(('10.242.11.167', 1234))
s.listen(5)
c = s.accept()
s = c[0]
ms = s.recv(10)
print ms