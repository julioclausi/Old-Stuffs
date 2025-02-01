person = {
    'name': 'John',
    'age': 33,
    'id': 1,
    'address': '305 Street X, City XXX'
}

print (person)

person['name'] = 'John Doe'

print (person)

##########

names = ['a', 'b', 'c']
numbers = [1,2,3]
test = dict.fromkeys(names,numbers)
print (test)

##########

contacts = {}
print ('*** Contacts ***')
while True:
    name = input('Name: ')
    phone = input('Phone: ')
    
    if name in contacts:
        if input(f'Name already registered with the number {contacts[name]}. Change? y/n ') == 'n':
            continue
    
    if phone in contacts.values():
        print ('Number already registered!')
        continue

    contacts[name]=phone

    if input('Quit? (y/n): ') == 'y':
        break
print (contacts)

remove_who = input ('Who do you want to remove? ')
print (contacts.pop(remove_who,'Contact not found'))
print (contacts)