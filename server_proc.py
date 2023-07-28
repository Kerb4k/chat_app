
from client import Client
from client import find_client
from chat import Chat
from chat import find_chat
import datetime

import os


class C:
    def __init__(self,c):
        self.c = c
    def c1(self):
        self.c += 1
    def gc(self):
        return self.c


def ms(client_address,client_socket, client_list,chat_list):

    cli = 0
    b = False
    print('Accepted new connection from {}:{}'.format(*client_address, ))

    while (True):
        m = client_socket.recv(100).decode('utf-8')


        if m == "":
            print('Closed connection from: {}'.format(client_socket))
            client_socket.close()
            find_client(client_list,usermame).offline(datetime.datetime.now().strftime('%H:%M:%S'))
            print(find_client(client_list,usermame).ro()[1])

        if m[0]+m[1] == "/u":
            p = m.split(" ")
            usermame = p[1]


            if len(client_list) == 0:
                client_list.append(Client(client_socket, client_address,usermame))
                cli = 1
                print("brand new user ", usermame)
            else:
                for i in range(len(client_list)):
                    if client_list[i].get_nick() == usermame:
                        client_list[i].change_ad(client_address)
                        client_list[i].change_s(client_socket)
                        client_list[i].get_messages()
                        b = True

                    else:
                        cli += 1
                if b == False:
                    client_list.append(Client(client_socket, client_address, usermame))
                    cli += 1
                    print("brand new user" , usermame)
                    b = True

            find_client(client_list,usermame).online()
        elif m[0]+m[1] == "/m":
            parts = m.split(" ")
            find_client(client_list, usermame).ch_ch(False)


            print("p", parts[1])
            find_client(client_list, usermame).set_rec(find_client(client_list, parts[1]))
            print(find_client(client_list, usermame).get_nick(), "reciver changed on",find_client(client_list, parts[1]).get_nick())
        elif m[0]+m[1] == "/c":
            p = m.split(" ")
            chat_list.append(Chat(p[1],find_client(client_list, usermame)))
            print("created chat", p[1])
            print("chat list 1",chat_list)
        elif m[0]+m[1] == "/h":

            p = m.split(" ")
            find_client(client_list, usermame).ch_ch(True)
            find_client(client_list, usermame).set_chat(p[1])
        elif m[0]+m[1] == "/a":
            p = m.split(" ")

            if (find_chat(chat_list, find_client(client_list,usermame).get_chat()).add_member(find_client(client_list,p[1]),find_client(client_list,usermame))==-1):
                find_client(client_list, usermame).get_socket().send("declined: u r not owner\n".encode('utf-8'))
            else:
                find_client(client_list, usermame).get_socket().send("Done\n".encode('utf-8'))
        elif m[0]+m[1] == "/n":
            p = m.split(" ")
            print("chat list 2", find_chat(chat_list,find_client(client_list, usermame).get_chat()).get_name())
            print("chat list 3", chat_list[0].get_name())
            print("chat list 4", p[1])
            #if find_chat(chat_list,p[1]).change_name(p[2], find_client(client_list,usermame)== -1):
            if find_chat(chat_list,find_client(client_list, usermame).get_chat()).change_name(p[1], find_client(client_list,usermame)) == -1:
                find_client(client_list, usermame).get_socket().send("declined: u r not owner\n".encode('utf-8'))
            else:
                find_client(client_list, usermame).get_socket().send("Done\n".encode('utf-8'))
                find_client(client_list, usermame).ch_ch(True)
                find_client(client_list, usermame).set_chat(p[1])

        else:
            if(find_client(client_list, usermame).get_ch() == False):
                if(find_client(client_list, usermame).get_rec().ro()[0] == True):
                    print(find_client(client_list, usermame).get_nick(), "|",  find_client(client_list, usermame).get_rec().get_nick())
                    mes = "{} ({}) > {}\n".format(usermame,datetime.datetime.now().strftime('%H:%M:%S'),m).encode('utf-8')
                    find_client(client_list,usermame).get_rec().get_socket().send(mes)
                    find_client(client_list, usermame).get_socket().send(mes)
                else:

                    mes = "the person was online last time at {}\n".format(find_client(client_list, usermame).get_rec().ro()[1]).encode('utf-8')
                    mes1 = "{} ({}) > {}\n".format(usermame, datetime.datetime.now().strftime('%H:%M:%S'), m).encode('utf-8')
                    find_client(client_list,usermame).get_socket().send(mes)
                    find_client(client_list, usermame).get_rec().new_messages((find_client(client_list, usermame),mes1))


            else:
                n = find_chat(chat_list,find_client(client_list, usermame).get_chat()).get_members()
                for i in range(len(n)):
                    if (n[i].ro()[0] == True):

                        b = "{} {} ({}) > {}\n".format(find_client(client_list, usermame).get_chat(), usermame,datetime.datetime.now().strftime('%H:%M:%S'), m).encode('utf-8')
                        w = "{} saw ur message\n".format(n[i].get_nick()).encode('utf-8')
                        find_client(client_list, usermame).get_socket().send(w)
                        n[i].get_socket().send(b)
                    else:
                        mes1 = "{} {} ({}) > {}\n".format(find_client(client_list, usermame).get_chat(), usermame,datetime.datetime.now().strftime('%H:%M:%S'), m).encode('utf-8')

                        n[i].new_messages((find_client(client_list, usermame),mes1))



        #
