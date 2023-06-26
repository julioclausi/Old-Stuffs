import numpy as np

class Array:
    def __init__(self,lenght):
        self.lenght = lenght
        self.last = -1
        self.values = np.empty(self.lenght,dtype=int)
        print (self.values)
    
    def printit(self):
        if self.last == -1:
            print ('Array is empty!')
        else:
            for i in range(self.last+1):
                print (f'{i} -> {self.values[i]}')
    
    def insert(self,num):
        if self.last == self.lenght - 1:
            print ('Array is Full')
            return

        position = 0
        for i in range(0,self.last+1):
            position = i
            if num < self.values[position]:
                break
            if i == self.last:
                position=i+1
        
        x = self.last
        while x >= position:
            self.values[x+1] = self.values[x]
            x-=1
        self.last+=1
        self.values[position] = num

my_array = Array(5)
my_array.printit()
my_array.insert(5)
my_array.insert(4)
my_array.insert(3)
my_array.insert(2)
my_array.insert(32)
my_array.insert(0)
my_array.printit()