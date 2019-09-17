if __name__ == "__main__": raise SystemError("Incorrect starting file")

import command
import connection

def user(user):
    command_list = user.command_list
    while command_list != []:
        c = command_list.pop()
        command.dictionary.funcs[c[0]](c[1])

def all(users = "Not_Given"):
    if users == "Not_Given": users = connection.users.copy()
    else: users = users.copy
    
    for user_ID in users:
        user = users[user_ID]
        command.execute.user(user)
    