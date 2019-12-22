if __name__ == "__main__": raise SystemError("Incorrect starting file")

import command
import connection

def user(user):
    command_list = user.command_list
    while command_list != []:
        c = command_list.pop()
        try: command.dictionary.funcs[c[0]](c[1])
        except KeyError:
            try: command.dictionary.methods[c[0]](user, c[1])
            except: raise SystemError("Unknown command")

def all(users = "Not_Given"):
    if users == "Not_Given": users = connection.users.copy()
    else: users = users.copy
    
    for user_ID in users:
        user = users[user_ID]
        try:
            command.execute.user(user)
        except Exception as error:
            print("Command error: ")
            print(error)
