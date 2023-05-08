#As a dev my first code needs to be a "Hello World"

print ("Hello World") #Hello World

#Let's start to study string

string_1 = "Hello"
string_2 = "World"
print (string_1 + string_2) #HelloWorld

#I realized I can use a + sign to concatenate two strings
#and the result of the code above is "HelloWorld"

print (string_1, string_2) #Hello World

#but now the result is "Hello World"
#the reason is:
#the function print has a parameter called sep and the default value is ' '

print ("123","789",sep='...') #123...789

print (string_1[0]) #H
print (string_1[1]) #e
print (string_1[2]) #l
print (string_1[3]) #l
print (string_1[4]) #o
#print (string_1[5]) ---> IndexError: string index out of range

string_1 = "My Code"
print(type(string_1)) #<class 'str'>

#type is not a function, is a callable

my_integer = 123
print(type(my_integer)) #<class 'int'>

#Can I change the type of a var?

my_integer = "A text"
print(type(my_integer)) #<class 'str'>

#the reason is: dynamic typing