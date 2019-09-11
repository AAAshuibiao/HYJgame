if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time

import connection

def wait_server_connected():
    addr = connection.server_addr
    try:
        assert len(addr.split('.')) == 4
        for ap in addr.split('.'):
            assert ap.isnumeric() and 0<=int(ap)<256
    except AssertionError:
        raise ValueError("Invalid server address")
    for t in range(100):
        if t%10 == 0: connection.send.server_connect_request()
        time.sleep(0.1)
