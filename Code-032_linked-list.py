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
