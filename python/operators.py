
# Operator Type	Operators

# Arithmetic	+ - * / // % **
# Comparison	== != > < >= <=
# Logical	and or not
# Bitwise	`&
# Assignment	= += -= *= /= //= %= **=
# Identity	is, is not
# Membership	in, not in
# 1. Arithmetic Operators
# Used for mathematical operations.

# Operator	Description	Example
# +	Addition	10 + 5 = 15
# -	Subtraction	10 - 5 = 5
# *	Multiplication	10 * 5 = 50
# /	Division	10 / 3 = 3.33
# //	Floor Division	10 // 3 = 3
# %	Modulus (Remainder)	10 % 3 = 1
# **	Exponentiation	2 ** 3 = 8

a, b = 10, 3
print(a + b)   
print(a - b)   
print(a * b)   
print(a / b)  
print(a // b) 
print(a % b)   
print(a ** b)  

# . Comparison (Relational) Operators
# Used to compare values and return True or False.

# Operator	Description	Example (a=10, b=5)
# ==	Equal to	a == b → False
# !=	Not equal to	a != b → True
# >	Greater than	a > b → True
# <	Less than	a < b → False
# >=	Greater than or equal to	a >= b → True
# <=	Less than or equal to	a <= b → False

a, b = 10, 5
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# 3. Logical Operators
# Used for logical operations (and, or, not).

# Operator	Description	Example
# and	Returns True if both conditions are True	(a > 5 and b < 10) → True
# or	Returns True if at least one condition is True	(a > 5 or b > 10) → True
# not	Reverses the result	not(a > 5) → False

a, b = 10, 5
print(a > 5 and b < 10)  
print(a > 5 or b > 10)  
print(not(a > 5))      


# 4. Bitwise Operators
# Used for operations on binary numbers.

# Operator	Description	Example (a=5 (0101), b=3 (0011))
# &	AND	5 & 3 → 1 (0001)
# `	`	OR
# ^	XOR	5 ^ 3 → 6 (0110)
# ~	NOT	~5 → -6
# <<	Left Shift	5 << 1 → 10 (1010)
# >>	Right Shift	5 >> 1 → 2 (0010)
a, b = 5, 3
print(a & b)  # Output: 1
print(a | b)  # Output: 7
print(a ^ b)  # Output: 6
print(~a)     # Output: -6
print(a << 1) # Output: 10
print(a >> 1) # Output: 2
# 5. Assignment Operators
# Used to assign values to variables.

# Operator	Example (x = 10)	Equivalent To
# =	x = 10	x = 10
# +=	x += 5	x = x + 5
# -=	x -= 3	x = x - 3
# *=	x *= 2	x = x * 2
# /=	x /= 2	x = x / 2
# //=	x //= 2	x = x // 2
# %=	x %= 3	x = x % 3
# **=	x **= 2	x = x ** 2
x = 10
x += 5  # x = x + 5 → x = 15
x *= 2  # x = x * 2 → x = 30
print(x)  # Output: 30


# 6. Identity Operators
# Used to compare object identity (memory location).

# Operator	Description	Example
# is	Returns True if both variables refer to the same object	x is y
# is not	Returns True if variables refer to different objects	x is not y
# 🔹 Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # Output: True (same memory reference)
print(a is c)   # Output: False (different objects)
print(a is not c)  # Output: True








