# Chapter 01

# Python is strongly, dynamically typed.

# Data types
# int, float, complex, bool, str, list, dict, tuple, set, frozenset

a = "Hello"
b = 1
c = 1.2
d = range(0,10,1)
e = list (d)
f = {'1':'A',
     '2':'B',
     '3':'C'}
g = ('a','b','c',4,5)
h = True
i = False
j = ['ABC','DEF','GHI',123,456]
print (type(a))
print (type(b))
print (type(c))
print (type(123+456j))
print (type(d))
print (type(e))
print (type(f))
print (type(g))
print (type(h))
print (type(i))
print (type(j))
print (type(None))

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'range'>
# <class 'list'>
# <class 'dict'>
# <class 'tuple'>
# <class 'bool'>
# <class 'bool'>
# <class 'list'>
# <class 'NoneType'>

# Numeric: int, float, complex
# Boolean: bool
# Sequence (immutable): str, tuple, range
# Sequence (mutable): list

# Identity: The 'is' operator is used to test if two variables refer to the same object
# Membership: 'in' or 'not in'

# Tuple: Immutable!

# Dict: {key:value}
# dict.clear()
# dict.get(<key>)
# dict.items()
# dict.keys()
# dict.values()
# dict.pop()
# dict.popitem()
# dict.update(<obj>)

# Set: mutable
# Frozenset: immutable

# Collections module: namedtuple, deque, defaultdict, Chainmap, Counter...

# Summary of Chapter 01: data types, some functions, collections, just the basics.

# Done! From page 18 to page 49