#How to read a file?

my_file = open("README.md", "r") #f become a TextIOWrapper

#Loop through the file line by line
# i = 1
# for line in my_file:
#     print (f'Line #{i}= {line}')
#     i += 1

#print(my_file.read()) #read all the file
#print(my_file.name) #print the name of the file

with my_file:
    list_of_lines = my_file.readlines()
print (list_of_lines)

my_file.close() 
#print(my_file.read()) #Afer close the file -> ValueError: I/O operation on closed file.
