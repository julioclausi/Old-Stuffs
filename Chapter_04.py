# Chapter 04

# Linked Lists

# Arrays = sequential list of data, each element is stored right after the previous one, arrays are very fast to access data

# Pointer Structures = lists of items that can be spread out in memory, don't require sequential storage space (but need aditional space to store the address)

# There are lot of pros and cons of both structures

class Node ():
    def __init__ (self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList ():
    def __init__ (self):
        self.head = None
    
    def __repr__ (self):
        finder = self.head
        while finder:
            print (finder.data,end=' -> ')
            finder = finder.next
        return '[None]'

    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def append_head(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head:
            current = self.head
            if current.next is None:
                self.head = None
            else:
                actual = current
                current = actual.next
                while current.next:
                    actual = current
                    current = current.next
                actual.next = None

list1 = SinglyLinkedList()
list1.pop()
print (list1)
list1.append('1')
print (list1)
list1.append('2')
print (list1)
list1.append_head('0')
print (list1)
list1.append('3')
print (list1)
list1.append('4')
print (list1)
list1.append_head('-1')
print (list1)
list1.pop()
print (list1)
list1.pop()
print (list1)
list1.pop()
print (list1)
list1.pop()
print (list1)
list1.pop()
print (list1)
list1.pop()
print (list1)
