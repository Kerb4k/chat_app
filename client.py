class Client:
    def __init__(self, s, ip, nick):
        self.__socket_number = s
        self.__ip= ip
        self.__nick = nick
        self.__messages = []
        self.__messages_from = []
        self.__unseen_messages = []
        self.__reciever = 0
        self.ch = False
        self.__chat = ""
        self.__online = False
        self.__lto = 0


    def offline(self,t):
        self.__lto = t
        self.__online = False
    def online(self):
        self.__online = True
    def ro(self):
        return  self.__online,self.__lto

    def new_messages(self, m):
        self.__messages.append(m)
    def get_messages(self):
        while len(self.__messages) > 0:
            self.__socket_number.send(self.__messages[0][1])
            self.__messages[0][0].get_socket().send(f"{self.__nick} saw ur message\n".encode('utf-8'))
            self.__messages.remove(self.__messages[0])


        return self.__messages
    def get_ip(self):
        return self.ip
    def get_nick(self):
        return self.__nick
    def get_socket(self):
        return self.__socket_number
    def change_ad(self, a):
        self.__ip = a
    def change_s(self,s):
        self.__socket_number = s
    def set_rec(self, r):
        self.__reciever = r
    def get_rec(self):
        return self.__reciever
    def ch_ch(self, c):
        self.ch = c
    def get_ch(self):
        return self.ch
    def set_chat(self,c):
        self.__chat = c
    def get_chat(self):
        return self.__chat

def find_client(list,nick):
    for i in range(len(list)):
        if list[i].get_nick() == nick:
            return list[i]



