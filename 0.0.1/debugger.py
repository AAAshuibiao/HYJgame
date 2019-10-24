import os
import socket

addr = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind( ("0.0.0.0", 10123) )

def send(c):
    s.sendto( bytes(c, "ascii"), (addr, 9912) )

while True:
    send(input())
