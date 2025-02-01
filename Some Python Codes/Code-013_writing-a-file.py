#Python File Write
# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)

my_file = open('my_file_for_code_013.txt', 'a')
my_file.write("My first line\n")
my_file.close()

#now open and read the file
my_file = open('my_file_for_code_013.txt', 'r')
print(my_file.read()) 
my_file.close()

my_file = open('my_file_for_code_013.txt', 'w')
my_file.write("OMG, I have deleted the content! <o>\n")
my_file.close()

#now open and read the file
my_file = open('my_file_for_code_013.txt', 'r')
print(my_file.read()) 
my_file.close()