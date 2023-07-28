class Chat:
    def __init__(self, n , o):
        self.__name = n
        self.__owner = o
        self.__p = [o]

    def change_name(self,n, p):
        if p == self.__owner:
            self.__name =n
            return 1
        else:
            return -1

    def get_name(self):
        return self.__name

    def add_member(self,m,p):

        if p == self.__owner:
            self.__p.append(m)
            return 1
        else:
            return -1
    def get_members(self):
        return self.__p


    def broadcast(self):
        pass

class Conversation:
    pass


def find_chat(l,n):
    for i in range(len(l)):
        if l[i].get_name() == n:
            return l[i]