if __name__ == "__main__": raise SystemError("Incorrect starting file")

import command

def all(command_list = command.default_source):
    while command_list != [] and command_list != "Server not connected":
        c = command_list.pop()
        command.dictionary.funcs[c[0]](c[1])
