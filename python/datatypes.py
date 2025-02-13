
# 1. Numeric Types
#Integer
x = 10 
print(type(x))
#Floating Point
y = 10.5 
print(type(y))
#Complex 
z = 2 + 3j  
print(type(z))  

# 2. Sequence Types
#String 
s = "Hello, Python!"
print(type(s)) 
# List
my_list = [1, 2, 3, "Python", 4.5]
print(type(my_list)) 
#Tuple 
my_tuple = (1, 2, 3, "Python")
print(type(my_tuple))
# . Set Types
# Set (set): Unordered, mutable collection with unique elements.

my_set = {1, 2, 3, 4, 4}  # Duplicate '4' is ignored
print(type(my_set))  # Output: <class 'set'>
# FrozenSet (frozenset): Immutable version of a set.

my_frozenset = frozenset([1, 2, 3, 4])
print(type(my_frozenset))  # Output: <class 'frozenset'>
my_dict = {"name": "Alice", "age": 25}
print(type(my_dict))  # Output: <class 'dict'>

#  4. Mapping Types
my_dict = {"name": "Alice", "age": 25}
print(type(my_dict))  # Output: <class 'dict'>
#  Boolean Type
# Boolean (bool): Represents True or False
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>

# 6. Binary Types
my_bytes = b"hello"
print(type(my_bytes))  # Output: <class 'bytes'>
# None Type
# NoneType (None): Represents the absence of a value.
nothing = None
print(type(nothing))  # Output: <class 'NoneType'>







