if __name__ == "__main__": raise SystemError("Incorrect starting file")

import connection

funcs = {
    "EXEC"  : exec                           ,\
    "PRINT" : print                          ,\
    "DOG"   : connection.connect.dog_respond ,\
}
