import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8001))

while True:
    s.sendto(bytes(input(),'ascii'), ('127.0.0.1',9912))
