# Chapter 02

# Principles of Algorithm Design
# As specific as possible
# Each instruction properly defined
# No ambiguous instruction
# Be executable in a finite amount of time and in a finite number of steps
# Clear input
# Clear output

# Big O notation (O)
# Omega notation (Ω)
# Theta notation (ϴ)

# O(1)     - Constant            - append, get item, set item
# O(logn)  - Logarithmic         - finding an element in a sort array
# O(n)     - Linear              - copy, insert, delete, iteration
# O(nLogn) - Linear-logarithmic  - sort a list, merge sort
# O(n²)    - Quadratic           - find the shortest path between two nodes in a graph
# O(n³)    - Cubic               - matrix multiplications
# O(2^n)   - Exponential         - towers of hanoi problem, backtracking

# Summary: basic of algorithm design and runtime

# Exercises:

# 1) Time complexity:

# a)
# i=1
# while (i<n):
#     i*=2
#     print('data')
# Answer: O(log(n))

# b)
# i = n
# while (i>1):
#     print('complexity')
#     i/=2
# Answer: O(log(n))

# c)
# for i in range(1,n):
#     j = i
#     while (j<n):
#         j*=2
# Answer: O(n*log(n))

# d)
# i = 2
# while (i<n):
#     print ('python')
#     i = i**2
# Answer: O(log2(log2(n)))

# Done! From page 50 to page 71