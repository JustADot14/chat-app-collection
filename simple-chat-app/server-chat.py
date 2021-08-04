import socket
import sys
import argparse
import threading

address = "127.0.0.1"
port = 4444
username = "Me"
clientname = "Received"

def recv_data(conn):
    while True:
        data=conn.recv(1024)
        print(f"\n{clientname}: {data.decode()}\n{username}: ", end="")

if __name__=="__main__":

    parser = argparse.ArgumentParser(description="Simple Chat Server Program.")
    parser.add_argument("-a", "--ipaddress", help="IP address of server (Default: 127.0.0.1)")
    parser.add_argument("-p", "--port", help="Port number to listen (Default: 4444)")
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
        s.bind((address, port))
        s.listen()
        print("\nServer address: " + address )
        print("Server listening port: " + str(port))
        print("\nWaiting for connection from client ...")
        try :
            conn, addr = s.accept()
        except KeyboardInterrupt:
            print("\nProgram exited.")
        except :
            print("\nError")
        else:
            print("\nConnected client IP: " + addr[0])
            print("Connected client port: " + str(addr[1]))
            print()
            conn.send(bytes(username, encoding="UTF-8"))
            clientname=conn.recv(1024)
            clientname=clientname.decode()
            recv_ = threading.Thread(target=recv_data, args=(conn,))
            recv_.start()
            while True:
                try: 
                    print(f"{username}: ", end="")
                    to_send = input()
                    conn.send(bytes(to_send, encoding="UTF-8"))
                except KeyboardInterrupt:
                    print("\nProgam Exited.")
                    conn.close()
                    s.close()
                    sys.exit()
                
        finally: 
            conn.close()
    except KeyboardInterrupt:
        print("\nProgam Exited.")
        s.close()
        sys.exit()
    finally:
        s.close()

