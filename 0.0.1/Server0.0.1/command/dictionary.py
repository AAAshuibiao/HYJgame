if __name__ == "__main__": raise SystemError("Incorrect starting file")

import connection

funcs = {
    "EXEC"  : exec  ,\
    "PRINT" : print
}

methods = {
    "ECHO" : connection.connect.echo        ,\
    "DOG"  : connection.connect.dog_respond
}
