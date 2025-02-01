import json

my_dict = {}
print (f'{my_dict=} is a {type(my_dict)}')

#we want to enter a country and a capital
#something like "Brazil": "Brasilia","Italy": "Rome"

def save_json (data):
    with open ('my_file_for_code_027.json', 'w') as f:
        json.dump(data,f,indent=4)
        f.close()

def read_json():
    data = {}
    try:
        with open ('my_file_for_code_027.json', 'r') as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        save_json({})
        return data

my_dict = dict(read_json())
print (my_dict)

while True:
    country = input('Digit a country or "quit" to leave: ')
    if country == 'quit':
        break
    capital = input(f'Digit the name of the capital of {country}: ')
    my_dict[country] = capital

print (my_dict)
save_json(my_dict)