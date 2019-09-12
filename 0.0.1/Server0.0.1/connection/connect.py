if __name__ == "__main__": raise SystemError("Incorrect starting file")

import random

import connection

class User(object):
    def __init__(self, ID, addr, playerName):
        self.ID = ID
        self.addr = addr
        self.name = playerName
        self.command_list = []

def accept(addr, playerName):
    if playerName == '': playerName = "Unnamed player"

    while True:
        ID = random.randint(0,100)
        if not ID in connection.users: break

    connection.users[ID] = User(str(ID), addr, playerName)
    
    connection.send.accept_connect_request(ID)
