def binary_search(my_list,left,right,element):
    middle = (left + right) // 2
    if left > right:
        print(f'{element} Not Found!')
        return
    print (f'From [{my_list[left]}] to [{my_list[right]}], checking [{my_list[middle]}]')
    if element == my_list[middle]:
        print(f'{element} Found!')
    elif element > my_list[middle]:
        binary_search(my_list,middle+1,right,element)
    elif element < my_list[middle]:
        binary_search(my_list,left,middle-1,element)
    else:
        print(f'{element} Not Found!')


my_list = []

for x in range(1,1025):
    my_list.append(x)

print (my_list)
binary_search(my_list,0,len(my_list)-1,16)
binary_search(my_list,0,len(my_list)-1,8)
binary_search(my_list,0,len(my_list)-1,24)
binary_search(my_list,0,len(my_list)-1,31)
binary_search(my_list,0,len(my_list)-1,32)
binary_search(my_list,0,len(my_list)-1,51)
binary_search(my_list,0,len(my_list)-1,1024)