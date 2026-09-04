# Notes: Functions in Python
#
# A function is a reusable piece of code that performs a specific task.
# Instead of writing the same logic again and again, we write it once
# inside a function, and just call the function whenever we need it.

# reuseable piece of code - specific task
# nums = [5, 18, 2, 5]
# total = 0
# for n in nums:
#     total = total + n
# print(total)

# Python already has a built-in function for this, so we do not need
# to write our own loop for something this common
# print(sum(nums))

# Functions -> Modules -> Packages-> Projects
# This shows how code gets organized as a project grows. Functions
# group code, modules group functions, packages group modules,
# and a project is made up of many packages.

# def fun_name():
    # reuseable piece of code
# def defines a function. The code inside a function only runs when
# the function is called, not when it is defined.

# def greet():
#     print("Hello")

# greet()

# greet()

# Calling the same function multiple times runs the same code again
# each time, without rewriting it
# greet()
# greet()
# greet()

# A function can accept input values, called parameters, so it can
# work with different data each time it is called
# def greet_1(name):
#     print("Hello", name)

# greet_1("Darshan")
# greet_1("Prem")
# greet_1("SAM")
# greet_1("Sunil")
# greet_1("Ram")

# A function can take more than one parameter
# def greet_2(name, name2):
#     print("Hello", name, name2)

# greet_2("Darshan", "ram")

# def sub_fuc(a, b):
#     print(a-b)
# sub_fuc(5, 3)

# return
# A function that only uses print() shows a value on the screen, but
# does not give the value back to the code that called it.
def add_print(a, b):
    print(a+b)
su = add_print(3, 5)
print(su)
# add_print() prints the sum, but does not return anything, so su
# ends up storing None, not the actual sum

# def add_return(a, b):
#     return a+b
# return sends a value back from the function, so it can be stored
# in a variable and used later, unlike print() which just displays it

# s= add_return(3, 5)
# print(s)
# print(s*s)

# Default parameter values
# If a parameter is not given a value when the function is called,
# it uses the default value instead
# def greet_default(name="user"):
#     print("Hello", name)
# greet_default("Sam")
# greet_default()

# def sub_fuc(a, b):
#     print(a-b)
# sub_fuc(5, 3)
# sub_fuc(3, 5)
# Arguments can also be passed using the parameter name directly,
# these are called keyword arguments, order does not matter here
# sub_fuc(a=5, b=3)
# sub_fuc(b=3, a =5)

# Positional only  / and keyword only *
# / marks that everything before it must be passed by position, not by name
# * marks that everything after it must be passed by name, not by position

# def example(a, b,/, c,*, d):
#     return a+b+c+d

# print(example(1, 2, 3, d=4))
# a and b must be positional here, so this fails since a and b are passed by name
# # print(example(a=1,b= 2,c= 3, d=4))
# print(example(1, 2,c= 3, d=4))

# A function can return more than one value at once, separated by commas.
# Python packs them together as a tuple.
# def arth(a, b):
#     return a+b, a-b, a*b

# res = arth(4, 5)
# print(res)
# The returned tuple can be unpacked directly into separate variables
# s, diff, prod = res
# print(s, diff, prod)
