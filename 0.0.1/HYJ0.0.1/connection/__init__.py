if __name__ == "__main__": raise SystemError("Incorrect starting file")


#//user config zone:
server_addr = "127.0.0.1"
ASKCONNECT_timeout_msec = 1000
ASKCONNECT_send_interval = 1000

playerName = "AAA_shuibiao"
#//end user config zone


ID = "Undefined"

__all__ = ["receive","connect","send"]
from connection import *
