if __name__ == "__main__": raise SystemError("Incorrect starting file")

import connection

default_source = connection.receive.command_list

__all__ = ["execute", "dictionary"]
from command import *
