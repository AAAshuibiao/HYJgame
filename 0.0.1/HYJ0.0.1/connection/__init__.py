if __name__ == "__main__": raise SystemError("Incorrect starting file")

def Check_Address_Validity(addr):
    try:
        assert len(addr.split('.')) == 4
        for ap in addr.split('.'):
            assert ap.isnumeric() and 0<=int(ap)<256
        return True
    except AssertionError:
        return False

#//user config zone:
server_addr = "127.0.0.1"
ASKCONNECT_timeout_msec = 1999
ASKCONNECT_send_interval = 1000

playerName = "AAA_shuibiao"
#//end user config zone

local_server_path = "D:\\mydata\\Programs\\HYJgame\\0.0.1\\Server0.0.1\\main.py"

while Check_Address_Validity( server_addr ) == False:
    print("input the local address:", end = '')
    server_addr = str( input() )

ID = "Undefined"

__all__ = ["receive","connect","send"]
from connection import *
