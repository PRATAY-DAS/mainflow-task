# This is a simple "Hello, World!" program
print("Hello, World!")

# Variables
x = 5
y = "Hello, World!"

# Printing variables
print(x)
print(y)

# Basic arithmetic operations
a = 10
b = 5

# Addition
sum = a + b
print("Sum:", sum)

# Subtraction
difference = a - b
print("Difference:", difference)

# Multiplication
product = a * b
print("Product:", product)

# Division
quotient = a / b
print("Quotient:", quotient)

# Modulus
remainder = a % b
print("Remainder:", remainder)

# String manipulation
s = "Hello, World!"

# Upper case
print(s.upper())

# Lower case
print(s.lower())

# Replace
print(s.replace("World", "Python"))

# Slicing
print(s[0:5])

# Conditional statements
num = 10

if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")


# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[1])

# Adding elements
fruits.append("orange")
print(fruits)

# Removing elements
fruits.remove("banana")
print(fruits)

# Tuples
colors = ("red", "green", "blue")
print(colors)

# Accessing elements
print(colors[1])

# Tuples are immutable, so we cannot add or remove elements, but we can concatenate them
new_colors = colors + ("yellow",)
print(new_colors)

# Dictionary with names and ages
people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}
print(people)

# Adding a new key-value pair
people["David"] = 40
print(people)

# Removing an existing key-value pair
del people["Bob"]
print(people)


# Check if a number is even or odd
number = 42

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


