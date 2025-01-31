class Node():
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

    def show (self):
        print (self.data)

class Arvore():
    def __init__ (self):
        self.raiz = None

    def insere (self,data):
        node = Node(data)
        if self.raiz is None:
            self.raiz = node
        else:
            current = self.raiz
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        return
                    else:
                        current = current.right

def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left)
    current.show()
    inorder(current.right)

arvore = Arvore()
lista = [4,8,7,2,9,10,5,1,3,6]

for i in lista:
    arvore.insere(i)

inorder(arvore.raiz)
#teste