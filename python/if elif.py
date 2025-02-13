# 1. Basic if Statement
# Executes a block of code only if the condition is True.
age = 18

if age >= 18:
    print("You are eligible to vote.")
#     2. if-else Statement
# Executes one block if the condition is True, otherwise executes another block.
num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
#     3. if-elif-else Statement
# Checks multiple conditions in sequence. The first True condition gets executed.
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    
    num = 15
#  4. Nested if Statements
# An if statement inside another if statement.
if num > 0:
    print("Positive number")
    if num % 5 == 0:
        print("Divisible by 5")
else:
    print("Negative number or zero")



