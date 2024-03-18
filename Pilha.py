# LIFO
# LAST IN, FIRST OUT

class Node:
    def __init__ (self,data=None):
        self.data = data
        self.next = None

class Pilha:
    def __init__ (self):
        self.head = None

    def show (self):
        current = self.head
        while current:
            print (current.data,end='->')
            current = current.next
        print ('Fim da pilha')

    def append (self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.show()

    def pop (self):
        if self.head:
            current = self.head
            self.head = current.next
        self.show()

pilha = Pilha()

senha = 1
escolha = ''

while escolha.capitalize() !='Q':
    escolha = input ('Digite o que quer fazer. [A]ppend [P]op [Q]uit: ')
    if escolha.capitalize() == 'A':
        pilha.append(senha)
        senha +=1
    elif escolha.capitalize() == 'P':
        pilha.pop()
    elif escolha.capitalize() == 'Q':
        ...
    else:
        print ('Comando inválido')