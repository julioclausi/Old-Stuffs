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

    def iter (self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append (self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

linked_list = SinglyLinkedList()

linked_list.append('First Node')
linked_list.append('Second Node')
linked_list.append('Third Node')

for node in linked_list.iter():
    print (node)