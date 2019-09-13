if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket

import connection

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind( ("0.0.0.0",8001) )

def string(ID, s):
    sender.sendto(bytes(s,'ascii'), (connection.users[ID].addr, 9912) )

def command(ID, command, content = '0'):
    connection.send.string(ID, command + ':' + content)

def accept_connect_request(ID):
    connection.send.command(ID, "ACCEPTCONNECT", connection.users[ID].ID)
