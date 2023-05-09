#How Can I add an int into a str?

string_1 = 'My text'
number_1 = 123

print (string_1, number_1) #My text 123

#result = string_1 + number_1 ---> TypeError: can only concatenate str (not "int") to str

result = string_1 + ' ' + str(number_1)
print (result) #My text 123
#It Works!
#str() is not a function, it's a class

string_2 = '5'
number_2 = int(string_2)
print ('This is a', type(number_2), 'and the value is', number_2)
#int() is not a function, it's a class
#I can convert float too