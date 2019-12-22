if __name__ == "__main__": raise SystemError("Incorrect starting file")

import random
import time

import connection


class User(object):
    def __init__(self, ID, addr, playerName):
        self.ID = ID
        self.addr = addr
        self.playerName = playerName
        self.command_list = []
        self.last_receive_time = time.time()

def accept(addr, playerName):
    if playerName == '': playerName = "Unnamed player"

    while True:
        ID = str(random.randint(0,10000))
        if not ID in connection.users: break

    connection.users[ID] = User(ID, addr, playerName)
    
    connection.send.accept_connect_request(ID)

def dog_check():
    for user_ID in connection.users.copy():
        user = connection.users[user_ID]
        if time.time() - user.last_receive_time > 5:
            connection.users.pop(user_ID)

def dog_respond(self, s):
    connection.send.command("DOG", "0", self.ID)

def echo(self, s):
    connection.send.command("PRINT", s, self.ID)
