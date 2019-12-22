if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket

import connection

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind( ("0.0.0.0",8001) )

def string(s, ID):
    sender.sendto( bytes(s, "ascii"), (connection.users[ID].addr, 9912) )

def command(command, content, ID):
    connection.send.string( command + ':' + content + ':' + ID , ID)

def accept_connect_request(ID):
    connection.send.command("ACCEPTCONNECT", connection.users[ID].ID, connection.users[ID].ID)
