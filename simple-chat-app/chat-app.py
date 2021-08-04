import socket
import sys
import argparse
import threading

# set default values
address = "127.0.0.1"
port = 4444
username = "Me"
othername = "Received"

def recv_data_thread(socketObj):
    while True:
        try:
            data=socketObj.recv(1024)
            print(f"\n{othername}: {data.decode()}\n{username}: ", end="")
        except ConnectionResetError:
            if othername!="Received":
                print(f"\nClosed by {othername}")
            else:
                print("\nClosed by other user.")
            break
        except ConnectionAbortedError:
            print(f"\nConnection closed by {username.lower()}.")
            break
    socketObj.close()
    print("Program Exited")
    sys.exit()


def server_func(address, port, username):
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
            s.close()
            sys.exit()
        except :
            print("\nError")
            s.close()
            sys.exit()
        else:
            print("\nConnected client IP: " + addr[0])
            print("Connected client port: " + str(addr[1]))
            print()
            conn.send(bytes(username, encoding="UTF-8"))
            global othername 
            othername = conn.recv(1024)
            othername = othername.decode()
            if othername=="Me":
                othername="Received"
            recv_ = threading.Thread(target=recv_data_thread, args=(conn,))
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
                except:
                    conn.close()
                    s.close()
                    sys.exit()
                
        finally: 
            conn.close()
    except KeyboardInterrupt:
        print("\nProgam Exited.")
        sys.exit()
    except:
        sys.exit()
    finally:
        s.close()

def client_func(address, port, username):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port)) 
        print("\nConnected Server IP: " + address)
        print("Connected Server port: " + str(port))
        print()
        global othername
        othername = s.recv(1024)
        othername = othername.decode()
        if othername=="Me":
            othername="Received"
        s.send(bytes(username, encoding="UTF-8"))
        recv_ = threading.Thread(target=recv_data_thread, args=(s,))
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
            except:
                s.close()
                sys.exit()
    except KeyboardInterrupt:
        print("\nProgam Exited.")
        sys.exit()
    except:
        sys.exit()
    finally:
        s.close()


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Simple Chat Program.")
    parser.add_argument("--server", help="Create a server", action="store_true")
    parser.add_argument("--client", help="Create a client", action="store_true")
    parser.add_argument("-a", "--ipaddress", help="IP address (Default: 127.0.0.1)")
    parser.add_argument("-p", "--port", help="Por number (Default: 4444)")
    parser.add_argument("-u", "--username", help="The name used during connection")
    
    args = parser.parse_args()
    
    if args.ipaddress:
        address=args.ipaddress
    if args.port:
        port=args.port
    if args.username:
        username=args.username

    if args.server:
        server_func(address, port, username)
    elif args.client:
        client_func(address, port, username)
    else :
        print("Type python chat-app.py -h for usage information.")
        print("Ctrl + C to exit the program.")
        try :
            input()
        except KeyboardInterrupt:
            sys.exit()
