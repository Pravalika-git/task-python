# #1. Numeric Data Types
# Python supports three main types of numeric data:

# (a) Integer (int)
# Represents whole numbers, both positive and negative.
x = 10  # Positive integer
y = -5  # Negative integer
z = 0   # Zero

print(type(x))  # Output: <class 'int'>

a = 3.14  # Positive float
b = -2.5  # Negative float

print(type(a))  # Output: <class 'float'>

c1 = 2 + 3j  
c2 = -1j    

print(type(c1))  # Output: <class 'complex'>

c1 = 2 + 3j  
c2 = -1j    

print(type(c1))  # Output: <class 'complex'>
num1 = 10
num2 = 3

print(num1 + num2)   # Addition -> 13
print(num1 - num2)   # Subtraction -> 7
print(num1 * num2)   # Multiplication -> 30
print(num1 / num2)   # Division -> 3.3333...
print(num1 // num2)  # Floor Division -> 3
print(num1 ** num2)  # Exponentiation -> 1000
print(num1 % num2)   # Modulus -> 1

# 2. String Data Type (str)
# A string is a sequence of characters enclosed in single ('), double ("), or triple (''' or """) quotes.
s1 = 'Hello'  
s2 = "Python"  
s3 = '''Multiline
String Example'''
  
print(type(s1))  # Output: <class 'str'>

str1 = "Hello"
str2 = "World"

# Concatenation
print(str1 + " " + str2)  # Output: Hello World

# Repetition
print(str1 * 3)  # Output: HelloHelloHello

# Indexing (0-based)
print(str1[0])  # Output: H
print(str1[-1]) # Output: o

# Slicing
print(str1[1:4])  # Output: ell (includes index 1 to 3)

# Length of string
print(len(str1))  # Output: 5

text = "python programming"

print(text.upper())   # Output: PYTHON PROGRAMMING
print(text.lower())   # Output: python programming
print(text.title())   # Output: Python Programming
print(text.replace("python", "Java"))  # Output: Java programming
print(text.split())   # Output: ['python', 'programming']





