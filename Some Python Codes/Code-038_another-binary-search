# Enter the lenght of the list: 16
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Log of 16 = 4.0
# Enter a number to find: 15
# ----------------------------------------------------------------
# [1 ] 2   3   4   5   6   7  [8 ] 9   10  11  12  13  14  15 [16]
# [LO]                                                        [HI]
#                             [MD]
# [Step 1]: Between 1 and 16, checking if 15 is equal to 8
# ----------------------------------------------------------------
#                                 [9 ] 10  11 [12] 13  14  15 [16]
#                                 [LO]                        [HI]
#                                             [MD]
# [Step 2]: Between 9 and 16, checking if 15 is equal to 12
# ----------------------------------------------------------------
#                                                 [13][14] 15 [16]
#                                                 [LO]        [HI]
#                                                     [MD]
# [Step 3]: Between 13 and 16, checking if 15 is equal to 14
# ----------------------------------------------------------------
#                                                         [15][16]
#                                                         [LO][HI]
#                                                         [MD]
# [Step 4]: Between 15 and 16, checking if 15 is equal to 15
# 15 found in position 14, steps=4

import math

def printing(list,low,high,mid,num,step):
    print('----'*len(list))
    for number in list:
        if number >= list[low] and number <= list[high]:
            if number == list[low] or number == list[high] or number == list[mid]:
                print(f'[{number:^2}]',end='')
            else:
                print(f'{number:^4}',end='')
        else:
            print('    ',end='')
    print ()
    print ('    '*low,'[LO]',sep='',end='')
    print ('    '*(high-low-1),'[HI]',sep='')
    print ('    '*mid,'[MD]',sep='')
    print (f'[Step {step}]: Between {list[low]} and {list[high]}, checking if {num} is equal to {list[mid]}')

def bin_search(list,num):
    steps = 0
    low = 0
    high = len(list)-1
    while low <= high:
        steps += 1
        mid = (low+high) // 2
        printing(list,low,high,mid,num,steps)
        if list[mid] < num:
            low = mid+1
        elif list[mid] > num:
            high = mid-1
        else:
            return f'{num} found in position {mid}, {steps=}'
    return f'{num} not found, {steps=}'

lenght = num = int(input('Enter the lenght of the list: '))
list = [i+1 for i in range(0,lenght)]
print (list)
print (f'Log of {lenght} = {math.log2(lenght)}')

num = int(input('Enter a number to find: '))
print(bin_search(list,num))
