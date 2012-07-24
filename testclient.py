import socket 

s = socket.socket()
s.connect (("10.242.11.167", 1234))
s.send('testing')