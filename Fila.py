class Node:
    def __init__ (self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
        self.data = None
        self.lenght = 0

    def iter (self):
        current = self.head
        while current:
            node = current
            current = node.next
            yield node

    def append (self,data):
        new_node = Node (data)
        if self.lenght:
            current = self.tail
            current.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.lenght +=1
        self.printing()

    def printing (self):
        for node in self.iter():
            print (node.data,end='->')
        print ('Fim da fila')

    def clear (self):
        self.__init__()

    def pop (self):
        if self.lenght:
            if self.lenght == 1:
                self.clear()
            else:
                current = self.head
                self.head = current.next
                self.lenght -=1
        else:
            print ('Fila vazia!')
            return
        self.printing()
        

fila = LinkedList()

senha = 1
escolha = ''

while escolha.capitalize() !='Q':
    escolha = input ('Digite o que quer fazer. [A]ppend [P]op [Q]uit: ')
    if escolha.capitalize() == 'A':
        fila.append(senha)
        senha +=1
    elif escolha.capitalize() == 'P':
        fila.pop()
    elif escolha.capitalize() == 'Q':
        ...
    else:
        print ('Comando inválido')