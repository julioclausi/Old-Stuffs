def selectionSort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

myArray = [9,8,7,6,5,4,3,2,1]
selectionSort(myArray)
print(myArray)
