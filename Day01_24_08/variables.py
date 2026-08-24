# Notes: Variables in Python
#
# A variable is a name given to a piece of data so we can use it again
# later, without typing the value every time. The pattern is always
# name = value. This is called assignment, and = is the assignment operator.
#
# Basic math operators can be used directly on numbers.
# print(8+5)   # addition
# print(2-5)   # subtraction
# print(8*5)   # multiplication
# print(2/5)   # division, always gives a float result

# a = 10
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Reassigning a variable
# A variable is not fixed. You can change its value at any time by
# assigning it again. The old value is replaced.

# x = 10
# print(x)
# x = 20
# print(x)

# Multiple assignment - same value
# All three variables below get the same value, 0

# a =0
# b=0
# c=0

# a = b= c= 0
# print(a, b, c)

# Multiple assignment - diff values
# Each variable gets its own value, matched in order.
# a gets 1, b gets 2, c gets 3, d gets 4

# a, b, c, d = 1, 2, 3, 4
# print(a, b, c, d)

# Rules for naming a variable:
# - Must start with a letter or an underscore _, never with a number.
# - Cannot contain spaces.
# - Can contain letters, numbers and underscores after the first character.
# - Cannot be a Python reserved word, such as if, else, for, class.
# - Variable names are case sensitive, so age, Age and AGE are three
#   different variables.

# abc = 12
# _abc = 15
# abc1 =17

# age = 14
# Age = 15
# AGE = 16

# # if, else, for, class are reserved words and cannot be used as variable names

# username = "Darshan"

# Naming styles used when a variable name has multiple words:
# snake_case user_name_one
# camelCase userNameOne
# PascalCase UserNameOne
# Python code usually follows snake_case for variable names.

# print() can take multiple values separated by commas
print("A","B","C")

# sep changes what is placed between the values, default is a space
print("A","B","C",sep="*")

# end changes what is added after the output, default is a new line.
# Here end="" removes the new line so the next print continues on the same line.
print("No newline", end="")
print(" next")
