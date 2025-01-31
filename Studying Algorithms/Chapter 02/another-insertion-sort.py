def insertionSort (A):
    for i in range(1,len(A)):
        key = A[i]
        print (f'{key=} e {i=}')
        j = i-1
        while (j>=0) and (A[j]>key):
            print (f'Comparando {key} com {A[j]}, {j=}')
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
        print(f'Array no momento: {A}')

# array = [5,2,4,6,1,3] #book case
array = [6,5,4,3,2,1] #worst case (15 interações)
# array = [1,2,3,4,5,6] #best case (5 interações)
print(array)
insertionSort(array)
print(array)
