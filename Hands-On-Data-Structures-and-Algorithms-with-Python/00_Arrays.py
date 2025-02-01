# Learning the concept about Arrays

# The id() function returns a unique id for the specified object
# https://docs.python.org/3/library/functions.html#id

MAX_LENGHT = 5

array = [None] * MAX_LENGHT

for i in range(0,MAX_LENGHT):
    array[i] = i
    print (id(array[i]))

# The result was:
# 140731377668872
# 140731377668904
# 140731377668936
# 140731377668968
# 140731377669000

# Conclusion:
# An array is a sequential list of data
# Each element is stored right after the previous one in memory
# Arrays are very fast to access elements since each element follows on from the previous one
# But if your array is really big and you are low in memory it could be impossible to find large enough storage to fit your entire array
# Arrays are very slow to insert and delete elements because you have to reorganize elements in the positions after the insertion/exclusion position

# https://docs.python.org/3/library/exceptions.html#MemoryError
# s = []
# for i in range(1000):
#    for j in range(1000):
#        for k in range(1000):
#            s.append("More")
# Exit: MemoryError