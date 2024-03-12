# Learning Linked Lists

# Properties:
# 1. List of items that can be spread out in memory and connected by pointers
# 2. The size of the list can increase or decrease during the execution of the program

# There are 3 types os lists:
# a. Singly
# b. Doubly
# c. Circular

# ______      ______      ______
# |data|      |data|      |data|
# |next| ---> |next| ---> |next| ---> None
# ‾‾‾‾‾‾      ‾‾‾‾‾‾      ‾‾‾‾‾‾

class Node():
    def __init__ (self, data=None):
        self.data = data
        self.next = None

# Here the pointer 'self.next' is inicialized with 'None', unless we change it, it's an endpoint

class SomeKindOfList():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def iter (self):
        """Iter the LL"""
        ...

    def clear (self):
        """Clear the LL"""
        ...

    def append (self, data):
        """Append the LL"""
        ...
    
    def append_at_a_location (self, data, index):
        ...
    
    def delete_first_node (self):
        ...
    
    def delete_last_node (self):
        ...
    
    def delete_specific_data (self, data):
        ...

    def delete_specific_index (self, index):
        ...

# Above an example of a Linked List and some functions that may exist