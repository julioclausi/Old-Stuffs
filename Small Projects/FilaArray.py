# [__,__,__,__, 5 , 6 , 7 , 8 ,__,__]
#               ^           ^
#              IN          OUT

MAX_SIZE = 3
SPACE = '       '

class FilaArray ():
    def __init__ (self):
        self.fila = [None] * MAX_SIZE
        self.first = 0
        self.last = 0
        self.size = 0

    def show (self):
        print ('-------'*MAX_SIZE)
        print ('|',end='')
        for item in self.fila:
            print (f'{str(item):^6}',end='|')
        print()
        print (f'{SPACE*self.first}   In')
        print (f'{SPACE*self.last}  Out')

    def enqueue (self,data):
        if self.size == MAX_SIZE:
            print ("Fila Cheia")
            return
        else:
            if self.size:
                self.last +=1
                if self.last >= MAX_SIZE:
                    self.last -= MAX_SIZE
                self.fila[self.last] = data
                self.size+=1
            else:
                self.fila[self.first] = data
                self.size +=1
        self.show()

    def dequeue (self):
        if self.size:
            print (f'Dequeue: {self.fila[self.first]}')
            self.fila[self.first] = None
            if self.size != 1:
                self.first +=1
                if self.first >= MAX_SIZE:
                    self.first -=MAX_SIZE
            self.size -=1
        else:
            print ("Fila vazia")
            return
        self.show()

fila = FilaArray()
fila.dequeue()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.dequeue()
fila.dequeue()
fila.enqueue(4)
fila.enqueue(5)
fila.enqueue(6)
fila.dequeue()
fila.dequeue()
fila.dequeue()
fila.dequeue()

# Fila vazia
# ---------------------
# |  1   | None | None |
#    In
#   Out
# ---------------------
# |  1   |  2   | None |
#    In
#          Out
# ---------------------
# |  1   |  2   |  3   |
#    In
#                 Out
# Fila Cheia
# Dequeue: 1
# ---------------------
# | None |  2   |  3   |
#           In
#                 Out
# Dequeue: 2
# ---------------------
# | None | None |  3   |
#                  In
#                 Out
# ---------------------
# |  4   | None |  3   |
#                  In
#   Out
# ---------------------
# |  4   |  5   |  3   |
#                  In
#          Out
# Fila Cheia
# Dequeue: 3
# ---------------------
# |  4   |  5   | None |
#    In
#          Out
# Dequeue: 4
# ---------------------
# | None |  5   | None |
#           In
#          Out
# Dequeue: 5
# ---------------------
# | None | None | None |
#           In
#          Out
# Fila vazia