# [] = list
# {} = dict

contacts = []
print (type(contacts))

for i in range(3):
    name = input('name ')
    phone = input('phone ')
    email = input('email ')
    new_contact = (name,phone,email)
    contacts.append(new_contact)

print (contacts)
for i in range(3):
    print (f'{i} = {contacts[i]}')

tuple1 = ('1','2','3')
tuple2 = ('4',)
sum_tuple = tuple1+tuple2 #concatenate
print (sum_tuple)