"""
from random import choice
print('Hello, world!')
print('What is your name?')
myName = input('Enter your name: ')
adjList = ['awesome', 'splendid', 'super', 'amazing']
print(f'Hello {myName}! It is {choice(adjList)} to meet you!')
"""

"""
# original
num = input("Type in a Number: ")
str = input("Type in a String: ")
print("num = ", num)
print("num is a ", type(num))
print("num * 2 = ", num * 2)
print("str = ", str)
print("str = ", str)
print("str * 2 = ", str * 2)
"""
"""
# modified
try:
    num = int(input("Type in a number: "))
except ValueError:
    print("Please enter a number.")
    exit()

str = input("Type in a string (words): ")
print("num = ", num)
print("num is a ", type(num))
print("num * 2 = ", num * 2)
print("str = ", str)
print("str = ", str)
print("str * 2 = ", str * 2)
"""
"""
# rectangle program
length = float(input("Length of the rectangle: "))
width = float(input("Width of the rectangle: "))
print(f"This rectangle has an area of {str(length * width)} units.")
print(f"This rectangle has a perimeter of {2 * length + 2 * width}")
"""

# temperature units
start = input("What is the starting unit? ").lower()
startVal = float(input("What is the value of the starting unit? "))
end = input("What is the end unit? ").lower()

if start == "f":
    if end == "c":
        endVal = (startVal - 32) * 5/9
    elif end == "k":
        endVal = (startVal - 32) * 5/9 + 273
if start == "c":
    if end == "f":
        endVal = startVal / (5/9) + 32
    elif end == "k":
        endVal = startVal / (5/9) + 32 - 273
print(endVal)
