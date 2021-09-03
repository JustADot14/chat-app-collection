# Start Date: 3/9/2021
# Last Updated: 3/9/2021
# Author: Lucifer 14
# App Name: Chat App (Multi Client)
# Version: CLI Version 1.0
# Type: Client

import socket
import threading
import time

def message_listener(socket_conn, get_username):
    while True:
        message = socket_conn.recv(1024).decode('utf-8')
        print("\n" + message + "\n" + get_username+": ", end="")

# connects to main_listener of server
def get_initial_connection(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    conn_recv = s.recv(100).decode('utf-8')
    user_id, portnumber, username = conn_recv.split(",")
    s.close()
    print("[+] Received: Username and port number from server\n")
    return user_id, portnumber, username

# connects to connection_listener of server
def main_connection(address, port):
    user_id, get_portnumber, get_username = get_initial_connection(address, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, int(get_portnumber)))
    s.send(bytes(user_id, encoding='utf-8'))
    recv_ = threading.Thread(target=message_listener, args=(s, get_username))
    recv_.start()
    while True:
        try :
            message = input("\n" + get_username + ": ")
        except KeyboardInterrupt:
            s.close()
            break
        else:
            s.send(bytes(get_username + ": " + message, encoding='utf-8'))


if __name__ == "__main__":
    address = "127.0.0.1"               # change server IP, don't forget to change in server
    port = 4444                         # change port number, don't forget to change in server
    main_connection(address, port)