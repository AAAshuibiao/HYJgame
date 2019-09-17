if __name__ == "__main__": raise SystemError("Incorrect starting file")

import random

import connection

def Phone_Call(self, name):
    print("Hello, " + name + "! This is " + self.playerName)

def echo(self, s):
    connection.send.command("PRINT", s, self.ID)
class User(object):
    def __init__(self, ID, addr, playerName):
        self.ID = ID
        self.addr = addr
        self.playerName = playerName
        self.command_list = []

def accept(addr, playerName):
    if playerName == '': playerName = "Unnamed player"

    while True:
        ID = str(random.randint(0,10000))
        if not ID in connection.users: break

    connection.users[ID] = User(ID, addr, playerName)
    
    connection.send.accept_connect_request(ID)
