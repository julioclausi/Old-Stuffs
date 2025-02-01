import json

def my_new_print (something,name='None'):
    print('-------------------------------')
    print (name)
    print (something)
    print (f'ID        = {id(something)}')
    print (f'Type      = {type(something)}')
    print (f'.values() = {something.values()}')
    print (f'.keys()   = {something.keys()}')
    print (f'.items()  = {something.items()}')
    print()

def save_json (data):
    with open ('my_file_for_code_028.json', 'w') as f:
        json.dump(data,f,indent=4)
        f.close()

def read_json():
    data = {}
    try:
        with open ('my_file_for_code_028.json', 'r') as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        save_json({})
        return data

data = read_json()

countries = data['Countries']
people = data ['People']
planets = data ['Planets']

my_new_print (people,'People')
my_new_print (countries,'Countries')
my_new_print (data['Countries'])

for my_types in data:
    #print (my_types)
    my_new_print(data[my_types],'Data My Types')
    for value, key in data[my_types].items():
        print (value,key,sep=' --- ')

if 'Brazil' not in data:
    print ('Brazil is not in data, is in Countries')

if 'Brazil' in data['Countries']:
    print ('Brazil discovered!')
    print ('Capital is',data['Countries'].get('Brazil'))

if 'Pluto' in planets:
    del planets['Pluto']
else:
    planets['Pluto'] = 'Pluto is no longer a planet'

print (planets)
print (data)

union = {
    'Countries': countries,
    'People': people,
    'Planets': planets
}

save_json(union)