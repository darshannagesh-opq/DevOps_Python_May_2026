# Notes: Understanding Errors in Python
#
# An error stops a program from running successfully. Different
# errors happen for different reasons, and knowing the type helps
# you fix the problem faster.

#  Syntax error
# A syntax error happens when the code is written incorrectly, and
# Python cannot even understand the structure of the line. The program
# does not run at all.

# print("Hello')
# Here the string starts with a double quote but ends with a single
# quote, so Python cannot tell where the string ends.

# Run time Error
# A runtime error happens while the program is running, even though
# the code itself is written correctly. The line causing it just
# cannot be completed during execution.

# print(10/0)
# Dividing by zero is mathematically not allowed, so this raises
# ZeroDivisionError while running.

# logical error
# A logical error does not crash the program or show any error message.
# The code runs fine, but gives the wrong result because the logic
# itself is incorrect.

# def add(a, b):
#     return a-b
# print(add(5, 3))
# This function is named add, but it actually subtracts, so it
# silently gives the wrong answer, 2, instead of 8

# Name error
# A name error happens when you use a variable or function name that
# has not been defined anywhere before.
# print(message)

# type Error
# A type error happens when an operation is used on data types that
# do not support it together.
# print("2" + 2)
# A string and an int cannot be added directly with +

# index error
# An index error happens when you try to access a position in a list
# that does not exist.

# nums = [1, 2, 4]
# print(nums[5])
# nums only has indexes 0, 1, 2, so index 5 does not exist

# key  error
# A key error happens when you try to access a dictionary key that
# does not exist.
# my_dict ={
#     "name" :"Sam"
# }
# print(my_dict['age'])
# "age" is not a key in my_dict

# Attribute error
# An attribute error happens when you call a method that does not
# exist for that data type.

# num = 5
# num.append(10)
# append() is a list method, not something an int has

# Indentation error
# An indentation error happens when the spacing of the code does not
# follow Python's indentation rules, so it cannot tell which lines
# belong inside a block.
# def add():
# print(2+3)
# The line after def add(): needs to be indented to show it belongs
# inside the function

# import error
# An import error happens when Python cannot find the module you are
# trying to import.
# import math
# import mathy
# There is no built-in module called mathy, so this fails

# Value error
# A value error happens when a value has the right data type, but its
# actual content is not valid for the operation being performed.

# print(int("3.14"))
# This fails, int() cannot directly convert a string that looks like
# a decimal number

# print(int("3"))
# This works fine, since "3" is a valid whole number as text


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Write a line of code that causes a NameError, then explain why
#    it happened.

# 2. Write a line of code that causes a TypeError by trying to add
#    a string and a number together.

# 3. Create a list with 3 items, then write code that causes an
#    IndexError by accessing an index that does not exist.

# 4. Create a dictionary with 2 keys, then write code that causes a
#    KeyError by accessing a key that does not exist.

# 5. Write a function with a logical error, where the function name
#    does not match what it actually does, similar to the add/subtract
#    example above.

# 6. Write a line of code that causes a ZeroDivisionError.

# 7. Write a line of code that causes an AttributeError by calling a
#    list method on an integer.

# 8. Try converting the string "12.5" directly to an int using int(),
#    and note which error this causes.

# 9. Write a function definition with an indentation mistake, and
#    note what error type this causes.

# 10. For each error type covered in this file (Syntax, Runtime,
#     Logical, Name, Type, Index, Key, Attribute, Indentation, Import,
#     Value), write one line in your own words describing when it happens.
