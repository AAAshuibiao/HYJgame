if __name__ == "__main__": raise SystemError("Incorrect starting file")

import command
import connection

def all(command_list = "Not_Given"):
    if command_list == "Not_Given":
        command_list = connection.receive.command_list
    while command_list != [] and command_list != "Server not connected":
        c = command_list.pop()
        command.dictionary.funcs[c[0]](c[1])
