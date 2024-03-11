# Learning the concept about node in Linked Lists
# Nodes are pointer structures
# A node is a container of data, together with one or more links to other nodes

class Node():
    def __init__(self, data=0,next_node=None):
        self.data = data
        self.next = next_node

first_node = Node(1) # create a node with data 1
print (f'First node address: {first_node}') # print the address of first_node
print (f'Data is: {first_node.data}') # print the data of first_node (here is 1)
print (f'Next node address: {first_node.next}') # print the address of the next node (here is None)
print ()
second_node = Node(2) # create a node with data 2
print (f'Second node address: {second_node}') # print the address of second_node
print (f'Data is: {second_node.data}') # print the data of second_node (here is 2)
print (f'Nex node address: {second_node.next}') # print the address of the next node (here is None)
print ()
first_node.next = second_node # linking the second_node in the first_node
print (f'Here the address of first_node.next ({first_node.next}) is the same of second_node ({second_node}).') # print the address of second_node

# The result was:
# First node address: <__main__.Node object at 0x000001AB1C48F690>
# Data is: 1
# Next node address: None
# 
# Second node address: <__main__.Node object at 0x000001AB1C48F750>
# Data is: 2
# Nex node address: None
# 
# Here the address of first_node.next (<__main__.Node object at 0x000001AB1C48F750>) is the same of second_node (<__main__.Node object at 0x000001AB1C48F750>).