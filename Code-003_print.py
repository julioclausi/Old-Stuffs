#Let's work with the print function

print ('Hello World') #Hello World
print ('This','and','that',sep='-',end='.END\n') #This-and-that.END

number = 123

print (f'String with a {number=}') #String with a number=123
print (f'String with a {number}') #String with a 123

number = 123.456789

print (number) #123.456789

#f string

print (f'{number:.2f}') #123.46
print (f'{number:.0f}') #123

#format

txt1 = "My name is {my_name}, I'm {my_age}".format(my_name = "Julio", my_age = 33)
txt2 = "My name is {0}, I'm {1}".format("Julio",33)
txt3 = "My name is {}, I'm {}".format("Julio",33) 
txt4 = "I'm {1}, my name is {0}".format("Julio",33) 

print (txt1) #My name is Julio, I'm 33
print (txt2) #My name is Julio, I'm 33
print (txt3) #My name is Julio, I'm 33
print (txt4) #I'm 33, my name is Julio

#Trying some stuffs

print (f'|{"Left align":<30}|')   #|Left align                    |
print (f'|{"Right align":>30}|')  #|                   Right align|
print (f'|{"Center align":^30}|') #|         Center align         |
print (f'|{"X":_^30}|')           #|______________X_______________|
print (f'|{"X":.^30}|')           #|..............X...............|
print (f'|{"X":-^30}|')           #|--------------X---------------|

#Let's play with some colors

#Thank you Li Haoyi https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

#ANSI code
# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m
# Reset: \u001b[0m

color = '\u001b[34m' #Blue
reset = '\u001b[0m' #Reset

print (f'{color}{"My Text"}{reset}') #My Text (blue)

# Background Black: \u001b[40m
# Background Red: \u001b[41m
# Background Green: \u001b[42m
# Background Yellow: \u001b[43m
# Background Blue: \u001b[44m
# Background Magenta: \u001b[45m
# Background Cyan: \u001b[46m
# Background White: \u001b[47m

background = '\u001b[43m'

print (f'{background}{"My Text"}{reset}') #My Text (yellow bg)

print ('-'*31)
print ('-'*31)
print (f"{'-'*13}{color}HELLO{reset}{'-'*13}")
print ('-'*31)
print ('-'*31)
#The 5 lines of code above will print this with 'HELLO' in blue
# -------------------------------
# -------------------------------
# -------------JULIO-------------
# -------------------------------
# -------------------------------