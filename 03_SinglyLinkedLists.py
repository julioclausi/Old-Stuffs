# Learning Singly Linked Lists

class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None

    def __str__ (self):
        return self.data

class SinglyLinkedList:
    def __init__ (self):
        self.head = None
        print ("List created!")

    def iter (self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append (self,data):
        print (f'\nAppending {data}')
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.print_list()

    def print_list (self):
        print ('Linked List: ',end='')
        for node in self.iter():
            print(node,end=' -> ')
        print('None')

    def clear (self):
        print ('Clearing the list')
        self.head = None

    def delete_last_node (self):
        print ('\nAttempt to remove the last node')
        if self.head is None:
            print ('Empty list')
        else:
            current = self.head
            prev = self.head
            if current.next is None:
                # Only one element, so clear the list
                print ('Only one element in the list')
                self.clear()
            else:
                while current.next:
                    prev = current
                    current = current.next
                prev.next = None
        self.print_list()

    def delete_first_node (self):
        print ('\nAttempt to remove the first node')
        if self.head is None:
            print ('Empty List')
        else:
            if self.head.next is None:
                # Only one element, so clear the list
                print ('Only one element in the list')
                self.clear()
            else:
                self.head = self.head.next
        self.print_list()

    def search(self,data):
        for node in self.iter():
            if data == node:
                return True
        return False

linked_list = SinglyLinkedList()
linked_list.append('[ABC]')
linked_list.append('[DEF]')
linked_list.append('[GHI]')
print ('\nSearching:')
print (f"[ABC]: {linked_list.search('[ABC]')}")
print (f"[XYZ]: {linked_list.search('[XYZ]')}")
linked_list.delete_last_node()
linked_list.delete_first_node()
linked_list.delete_last_node()
linked_list.delete_last_node()

# The result was:
# List created!

# Appending [ABC]
# Linked List: [ABC] -> None

# Appending [DEF]
# Linked List: [ABC] -> [DEF] -> None

# Appending [GHI]
# Linked List: [ABC] -> [DEF] -> [GHI] -> None

# Searching:
# [ABC]: True
# [XYZ]: False

# Attempt to remove the last node
# Linked List: [ABC] -> [DEF] -> None

# Attempt to remove the first node
# Linked List: [DEF] -> None

# Attempt to remove the last node
# Only one element in the list
# Clearing the list
# Linked List: None

# Attempt to remove the last node
# Empty list
# Linked List: None