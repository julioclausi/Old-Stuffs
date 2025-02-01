names = []

while True:
    name = input('Name: ')
    if name == 'quit':
        break
    last_name = input('Last name: ')
    full_name = [name,last_name]
    names.append(full_name)

for name in names:
    print(f'{name[1]}, {name[0]}')