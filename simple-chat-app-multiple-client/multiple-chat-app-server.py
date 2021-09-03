# Start Date: 3/9/2021
# Finished Date: 3/9/2021
# Author: Lucifer 14
# App Name: Chat App (Multi Client)
# Version: CLI Version 1.0
# Type: Server

import socket
import random
import threading

connection_list=[]

# generates random portnumber for client
def random_port_generator(address):
    result_of_check = 0
    while result_of_check == 0:
        random_port_number = random.randint(10000, 20000)
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = a_socket.connect_ex((address, random_port_number))
        a_socket.close()
        if result_of_check != 0:
            break
    print("[+] Generated: New port number: "+ str(random_port_number) +"\n")
    return random_port_number

# forwards the message to all clients
def forward_message(get_user_id, recv_msg):
    conn_list=[]
    for i in range(len(connection_list)):
        if connection_list[i][0] != get_user_id and connection_list[i][4]=='1':
            conn_list.append(connection_list[i][5])
    for conn in conn_list:
        conn.send(recv_msg)

# listens for main_connection from client
def connection_listener(address, port, modified_username):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen()
    conn, addr = s.accept()
    get_user_id = conn.recv(1024).decode('utf-8')
    print("[+] Connected: User ID: " + get_user_id+ ", Username: " + modified_username +"\n\n")
    for i in range(len(connection_list)):
        if connection_list[i][0] == get_user_id:
            connection_list[i].append(conn)
    
    while True:
        try:
            recv_msg = conn.recv(1024)
        except:
            msg = bytes("Server: " + modified_username + " has left the chat.", encoding='utf-8')
            print("[-] Disconnected: User ID: " + get_user_id+ ", Username: " + modified_username)
            forward_message(get_user_id, msg)
            for i in range(len(connection_list)):
                if connection_list[i][5] == conn and connection_list[i][4]=='1':
                    connection_list[i][4] = '0'
                    print("[-] Removed: Client info from connection list\n\n")
                    break
            conn.close()
            s.close()
            break
        else:
            forward_message(get_user_id, recv_msg)


# listens for get_initial_connection from client
def main_listener(address, port, username):
    random_port_number = random_port_generator(address)
    user_id = str(len(connection_list)+1)
    modified_username = username+user_id
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen()
    conn, addr = s.accept()
    to_send = user_id + "," + str(random_port_number) + "," + modified_username
    conn.send(bytes(to_send, encoding='utf-8'))
    conn.close()
    s.close()
    print("[+] Sent: Username: " + modified_username + ", Port number: " + str(random_port_number))
    connection_list.append([user_id, modified_username, addr[0], random_port_number, '1'])
    print("[+] Added: New client info in connection list\n")
    new_connection = threading.Thread(target=connection_listener, args=(addr[0], random_port_number, modified_username))
    new_connection.start()

    

if __name__ == "__main__":
    address = "127.0.0.1"       # change server IP, don't forget to change in client
    port = 4444                 # change port number, don't forget to change in client
    username = "User"           # change Username
    while True:
        main_listener(address, port, username)
