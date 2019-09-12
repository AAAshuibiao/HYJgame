import time

import connection

while True:
    for user_ID in connection.users:
        user = connection.users[user_ID]
        print("Name: " + user.name + "     ID: " + str(user.ID))
        print("Command: ", end = '')
        for command in user.command_list:
            print(command, end = ', ')
        print('\n\n')
    time.sleep(1)
