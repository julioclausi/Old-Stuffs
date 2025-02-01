# Chapter 04

# Linked Lists

# Arrays = sequential list of data, each element is stored right after the previous one, arrays are very fast to access data

# Pointer Structures = lists of items that can be spread out in memory, don't require sequential storage space (but need aditional space to store the address)

# There are lot of pros and cons of both structures

# class Node ():
#     def __init__ (self, data=None):
#         self.data = data
#         self.next = None

# class SinglyLinkedList ():
#     def __init__ (self):
#         self.head = None
    
#     def __repr__ (self):
#         finder = self.head
#         while finder:
#             print (finder.data,end=' -> ')
#             finder = finder.next
#         return '[None]'

#     def append(self,data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = node
    
#     def append_head(self,data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node

#     def pop(self):
#         if self.head:
#             current = self.head
#             if current.next is None:
#                 self.head = None
#             else:
#                 actual = current
#                 current = actual.next
#                 while current.next:
#                     actual = current
#                     current = current.next
#                 actual.next = None

# list1 = SinglyLinkedList()
# list1.pop()
# print (list1)
# list1.append('1')
# print (list1)
# list1.append('2')
# print (list1)
# list1.append_head('0')
# print (list1)
# list1.append('3')
# print (list1)
# list1.append('4')
# print (list1)
# list1.append_head('-1')
# print (list1)
# list1.pop()
# print (list1)
# list1.pop()
# print (list1)
# list1.pop()
# print (list1)
# list1.pop()
# print (list1)
# list1.pop()
# print (list1)
# list1.pop()
# print (list1)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return "[" + str(self.head) + "]"

class Node:
    def __init__(self, data=0,next_node=None):
        self.data = data
        self.next = next_node
    
    def __repr__(self):
        return f'{self.data} -> {self.next}'

def insert_at_beginning(list,data):
    new_node = Node(data)
    new_node.next = list.head
    list.head = new_node
    print(list)

def insert_at_end(list,data):
    finder=list.head
    while finder.next is not None:
        finder = finder.next
    new_node = Node(data)
    finder.next = new_node
    print(list)
    
def print_list(list):
    finder=list.head
    print('[',end='')
    while finder is not None:
        print(finder.data,end=' -> ')
        finder = finder.next
    print('None]')

def search(list,data):
    finder = list.head
    while finder is not None:
        if data == finder.data:
            return True
        finder = finder.next
    return False

def remove_the_first_one(list):
    list.head = list.head.next
    print(list)

def remove(list,data):
    finder = list.head
    removed = False
    if finder.data == data:
        list.head = finder.next
    else:
        while finder.next != None and not removed:
            previous = finder
            finder = previous.next
            if finder.data == data:
                previous.next = finder.next
                print(f'{data} is removed!')
                removed = True
    if not removed:
        print(f'{data} is not removed!')

while True:
    command = input('[C]reate List, [A]dd, [E] add at end, [Y] Add 1 to 5, [P]rint, [S]earch, [R]emove, [Q]uit: ')
    if command.lower() == 'c':
        print('Creating...')
        my_list = LinkedList()
        print ('List Created ->',my_list)

    elif command.lower() == 'a':
        data = input('Enter a value: ')
        print('Adding...')
        insert_at_beginning(my_list,data)
        
    elif command.lower() == 'y':
        for i in range(1,6):
            insert_at_beginning(my_list,str(i))
        
    elif command.lower() == 'e':
        data = input('Enter a value: ')
        print('Adding...')
        insert_at_end(my_list,data)

    elif command.lower() == 'q':
        print ('Quit!')
        break

    elif command.lower() == 'p':
        print ('Printing...')
        print_list(my_list)
        
    elif command.lower() == 'r':
        data = input('Enter a value: ')
        print ('Removing...')
        remove(my_list,data)

    elif command.lower() == 's':
        data = input('Enter a value: ')
        print ('Searching...')
        if search(my_list,data):
            print ('Found')
        else:
            print('Not found')
