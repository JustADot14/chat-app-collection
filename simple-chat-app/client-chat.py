import socket
import sys
import argparse
import threading

address = "127.0.0.1"
port = 4444
username = "Me"
servername = "Received"

def recv_data(s):
    while True:
        data=s.recv(1024)
        print(f"\n{servername}: {data.decode()}\n{username}: ", end="")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Simple Chat Client Program.")
    parser.add_argument("-a", "--ipaddress", help="IP address of target server (Default: 127.0.0.1)")
    parser.add_argument("-p", "--port", help="Listening port number of target server (Default: 4444)")
    parser.add_argument("-u", "--username", help="The name used during connection")

    args = parser.parse_args()
    if args.ipaddress:
        address=args.ipaddress
    if args.port:
        port=args.port
    if args.username:
        username=args.username

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port)) 
        print("\nConnected Server IP: " + address)
        print("Connected Server port: " + str(port))
        print()
        servername=s.recv(1024)
        servername=servername.decode()
        s.send(bytes(username, encoding="UTF-8"))
        recv_ = threading.Thread(target=recv_data, args=(s,))
        recv_.start()
        while True:
            try: 
                print(f"{username}: ",end="")
                to_send=input()
                s.send(bytes(to_send, encoding="UTF-8"))
            except KeyboardInterrupt:
                print("\nProgam Exited.")
                s.close()
                sys.exit()
    except KeyboardInterrupt:
        print("\nProgam Exited.")
        s.close()
        sys.exit()
    finally:
        s.close()