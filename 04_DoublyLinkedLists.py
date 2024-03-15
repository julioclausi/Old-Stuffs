# Learning Doubly Linked Lists

class Node:
    def __init__ (self,data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None

    def iter (self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def printing (self):
        for data in self.iter():
            print (data,end=' -> ')
        print ('None')

    def append (self,data):
        new_node = Node(data)
        if self.head == None:
            #Empty list
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def printing_backwards (self):
        current = self.tail
        while current:
            print (current.data,end=' -> ')
            current = current.prev
        print ('None')

    def append_new_data_after_some_data (self,new_data,some_data):
        node = self.head
        while node:
            if node.data == some_data:
                new_node = Node(new_data)
                new_node.next = node.next
                new_node.prev = node
                if node.next:
                    next = node.next
                    next.prev = new_node
                    new_node.next = next
                node.next = new_node
                return
            node = node.next

    def delete (self,data):
        print (f'\nTrying to remove {data}')
        node = self.head

        if self.head == self.tail:
            # Only one element in the list
            if node.data == data:
                self.head = None
                self.tail = None
                return

        if node.data == data:
            # Found in the first node
            next = node.next
            self.head = next
            next.prev = None
            return

        node = self.tail
        if node.data == data:
            # # Found in the last node
            prev = node.prev
            prev.next = None
            self.tail = prev
            return
        
        node = self.head
        while node:
            if data == node.data:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
                return
            node = node.next
        
        print (f'There is no {data} here.')


my_list = DoublyLinkedList()
my_list.append('Athos')
my_list.append('Porthos')
my_list.append('Aramis')
my_list.append_new_data_after_some_data('Dartagnan','Porthos')
my_list.printing()
my_list.printing_backwards()
my_list.delete('Cardinal Richelieu')
my_list.printing()
my_list.printing_backwards()
my_list.delete('Dartagnan')
my_list.printing()
my_list.printing_backwards()
my_list.delete('Athos')
my_list.printing()
my_list.printing_backwards()
my_list.delete('Aramis')
my_list.printing()
my_list.printing_backwards()
my_list.delete('Porthos')
my_list.printing()
my_list.printing_backwards()

# The result was:
# Athos -> Porthos -> Dartagnan -> Aramis -> None
# Aramis -> Dartagnan -> Porthos -> Athos -> None

# Trying to remove Cardinal Richelieu
# There is no Cardinal Richelieu here.
# Athos -> Porthos -> Dartagnan -> Aramis -> None
# Aramis -> Dartagnan -> Porthos -> Athos -> None

# Trying to remove Dartagnan
# Athos -> Porthos -> Aramis -> None
# Aramis -> Porthos -> Athos -> None

# Trying to remove Athos
# Porthos -> Aramis -> None
# Aramis -> Porthos -> None

# Trying to remove Aramis
# Porthos -> None
# Porthos -> None

# Trying to remove Porthos
# None
# None