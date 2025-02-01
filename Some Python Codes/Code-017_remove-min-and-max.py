my_list = [13,25,42,33,12,5,55,5]

print(my_list)
my_min = min(my_list)
my_max = max(my_list)

if my_list.count(my_min) == 1:
    my_list.remove(my_min)
    print('Removing', my_min)
else:
    for i in range(len(my_list)):
        if my_list[i] == my_min:
            print('Removing', my_min)
            my_list.pop(i)
            break

if my_list.count(my_max) == 1:
    my_list.remove(my_max)
    print('Removing', my_max)
else:
    for i in range(len(my_list)):
        if my_list[i] == my_max:
            print('Removing', my_max)
            my_list.pop(i)
            break
    
print (my_list)
