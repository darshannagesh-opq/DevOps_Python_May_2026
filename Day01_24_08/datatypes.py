# Notes: Data Types in Python
#
# A data type tells Python what kind of value is being stored, and
# what can be done with it. Python decides the data type automatically
# based on the value you give it, you do not need to declare it.
#
# The four basic data types are int, float, str and bool.
# int    - whole numbers, positive, negative or zero: -1, -5, 0, 1, 1000
# float  - numbers with a decimal point: 1.5, -3.6, 0.5, 2.33333
# str    - text inside single or double quotes: "Sam", 'sam'
# 'a" - a string should start with a quote and end with the same type of quote
# bool   - only two possible values: True or False

# Whole numbers, positive or negative, are of type int
# print(0)
# print(-5)
# print(-1000)
# print(type(12345))

# Numbers with a decimal point are of type float
# print(1.5, type(1.5))

# type() is a built-in function that tells us the data type of any value
print(type(10))    # int, a whole number
print(type(10.0))  # float, a decimal number
print(type("10"))  # str, because it is inside quotes, so it is text, not a number
# print("Sam", type("Sam"))
# print('sam')

# If your text contains an apostrophe, like Sam's, using single quotes
# around the whole string can confuse Python. Double quotes are safer here.
# print("Sam's")

# bool has only two possible values, True or False, and both start with a capital letter
print(True, type(True))

# Key points:
# - Numbers without quotes are int or float.
# - Anything inside quotes is a string, even if it looks like a number.
#   For example 10 is a number, but "10" is text.
# - Use type() whenever you want to check what kind of value you are working with.
