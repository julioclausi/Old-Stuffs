from collections import namedtuple

my_list = []
TupleSomething = namedtuple("TupleSomething", ['name','id'])

while True:
    name = input('name: ')
    id = input('id: ')
    something = TupleSomething(name=name,id=id)
    my_list.append(something)
    if input('quit? (q)') == 'q':
        break

for something in my_list:
    print (f'Name {something.name}')
    print (f'ID {something.id}',end='\n-----\n')
