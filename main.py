import socket
import select

from threading import *

from client import Client
from client import find_client
from chat import Chat

from server_proc import ms
from server_proc import C
HEADER_LENGTH = 50
# Handles message receiving

client_list = []
b = False
chat_list = []

list = []
c = C(0)


def ip6(client_list,b,chat_list, list,c):
    IP6 = "fe80::f3e3:636f:1dee:7612"
    IP4 = "10.100.30.55"
    PORT6 = 1234
    PORT4 = 1235

    # Create a socket
    # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
    # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    #server_socket4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # SO_ - socket option
    # SOL_ - socket option level
    # Sets REUSEADDR (as a socket option) to 1 on socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #server_socket4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind, so server informs operating system that it's going to use given IP and port
    # For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
    #server_socket.bind((IP, PORT))
    server_socket.bind(('', 1234))
    #server_socket4.bind((IP4,PORT4))
    # This makes server listen to new connections
    server_socket.listen()
    #server_socket4.listen()

    # List of sockets for select.select()
    sockets_list = [server_socket]
    #sockets_list4 = [server_socket4]

    # List of connected clients - socket as a key, user header and name as data
    clients = {}
    clients4 = {}

    print(f'Listening for connections on {IP6}:{PORT6}...')


    # Handles message receiving


    while True:

        client_socket, client_address = server_socket.accept()
        #client_socket, client_address = server_socket4.accept()
        list.append(Thread(target = ms,args=(client_address,client_socket,client_list,chat_list)))
        c.c1()
        list[c.gc()-1].start()
def ip4(client_list, b, chat_list, list, c):
    IP6 = "fe80::f4ec:50fd:141b:c0ea"
    IP4 = "192.168.0.101"
    PORT6 = 1234
    PORT4 = 1235

    # Create a socket
    # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
    # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # SO_ - socket option
    # SOL_ - socket option level
    # Sets REUSEADDR (as a socket option) to 1 on socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # server_socket4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind, so server informs operating system that it's going to use given IP and port
    # For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
    # server_socket.bind((IP, PORT))
    #server_socket.bind(('2001:708:150:10::67d9', 1234))
    server_socket.bind((IP4,PORT4))
    # This makes server listen to new connections
    server_socket.listen()
    # server_socket4.listen()

    # List of sockets for select.select()
    sockets_list = [server_socket]
    # sockets_list4 = [server_socket4]

    # List of connected clients - socket as a key, user header and name as data
    clients = {}
    clients4 = {}


    print(f'Listening for connections on {IP4}:{PORT4}...')

    # Handles message receiving

    while True:
        client_socket, client_address = server_socket.accept()
        # client_socket, client_address = server_socket4.accept()
        list.append(Thread(target=ms, args=(client_address, client_socket, client_list, chat_list)))
        c.c1()
        list[c.gc() - 1].start()


q1 = Thread(target=ip6, args= [client_list,b,chat_list, list,c])
q2 = Thread(target=ip4, args= [client_list,b,chat_list, list,c])

q1.start()
q2.start()



