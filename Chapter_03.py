# Chapter 03

# Algorithm Design Techniques and Strategies

# Recursion
# def factorial (n):
#     # base case
#     if n==0:
#         return 1
#     # do a calculation and a recursive call
#     return n*factorial(n-1)

# Divide and conquer
# Used in: binary search, merge sort, quick sort, matrix multiplication (Strassen), fast multiplication (Karatsuba), closest pair of points

    # Binary Search
    # def binary_search(arr,start,end,key):
    #     while start <= end:
    #         mid = int(start + (end - start)/2)
    #         if arr [mid] == key:
    #             return mid
    #         elif arr [mid] < key:
    #             start = mid +1
    #         else:
    #             end = mid - 1
    #     return -1
    # arr = [10,20,30,40,50,60,70,80,90]
    # x = 70
    # result = binary_search(arr,0,len(arr)-1,x)
    # print (result)

    # Merge Sort
    # def merge(first_sublist,second_sublist):
    #     i = j = 0
    #     merged_list = []
    #     while i < len(first_sublist) and j < len(second_sublist):
    #         if first_sublist[i] < second_sublist[j]:
    #             merged_list.append(first_sublist[i])
    #             i+=1
    #         else:
    #             merged_list.append(second_sublist[j])
    #             j+=1
    #     while i < len(first_sublist):
    #         merged_list.append(first_sublist[i])
    #         i+=1
    #     while j < len(second_sublist):
    #         merged_list.append(second_sublist[j])
    #         j+=1
    #     return merged_list
    # def merge_sort(unsorted_list):
    #     if len(unsorted_list) == 1:
    #         return unsorted_list
    #     mid_point = int(len(unsorted_list)/2)
    #     first_half = unsorted_list[:mid_point]
    #     second_half = unsorted_list[mid_point:]
    #     half_a = merge_sort(first_half)
    #     half_b = merge_sort(second_half)
    #     return merge(half_a,half_b)
    # print (merge_sort([9,8,7,6,5,4,3,2,1]))

# Dynamic programming
# This technique starts from the initial problem set and divides it into small subproblems
    # Fibonacci problem
    # def fib(n):
    #     if n <= 1:
    #         return 1
    #     else:
    #         return fib(n-1) + fib(n-2)
    # for i in range(5):
    #     print (fib(i))

    # Memoization technique

    # The idea here is to save pre calculated values
    # def dyna_fib(n): 
    #     if n == 0: 
    #         return 0 
    #     if n == 1: 
    #         return 1   
    #     if lookup[n] is not None: 
    #         return lookup[n] 
    #     lookup[n] = dyna_fib(n-1) + dyna_fib(n-2) 
    #     return lookup[n] 
    # lookup = [None]*(1000) 
    # for i in range(6):  
    #     print(dyna_fib(i)) 

# Greedy algorithms
# Prim, Dijkstra, Kruskal, Traveling salesman problem...

# Summary: a general look about algorithm design techniques. 

# Done! From page 72 to page 104