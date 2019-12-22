if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket

import connection

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind( ("0.0.0.0",9999) )

def string(s):
    sender.sendto( bytes(s, "ascii"), (connection.server_addr, 8000) )

def command(command, content = 0, ID = "Not_Given"):
    if ID == "Not_Given":
        if connection.ID != "Undefined":
            ID = connection.ID
        else: raise SystemError("ID Undefined")
    connection.send.string(command + ':' + content + ':' + ID)

def ask_connect_request(playerName):
    connection.send.command("ASKCONNECT", playerName, "Undefined")
