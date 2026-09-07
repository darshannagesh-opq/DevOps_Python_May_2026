# Notes: Functions Part 2 (Scope, *args, **kwargs, Type Hints)

# g = 10
# A variable created outside any function is called a global variable.
# It can be read from inside a function.

# def scope_demo():
#     l = 5
#     print("inside func : ", g, l)
#     return l
# l here is a local variable, it only exists inside this function,
# it is created when the function runs and is gone once it finishes.
# g is a global variable, so it can still be read inside the function
# without any special steps.

# scope_demo()
# l = 11
# print("outside func : ", g, l)
# This l is a different variable from the l inside scope_demo(), even
# though they share the same name. A local variable does not affect
# a variable with the same name outside the function.

# # *args , **kwargs
# Normally a function needs a fixed number of arguments. *args and
# **kwargs let a function accept any number of extra arguments.


# def many_args(a, *args, **kwargs):
#     print("a: ", a)
#     print("args: ", args)
#     print("kwargs: ", kwargs)
# *args collects any extra positional arguments into a tuple
# **kwargs collects any extra keyword (name=value) arguments into a dict


# many_args(1, 2, 3, 4, name="Sam", age=30)
# Here a = 1, args = (2, 3, 4), kwargs = {"name": "Sam", "age": 30}

#  Type hints
# Type hints suggest what data type a parameter or return value is
# expected to be. They are just hints for readability, Python does
# not actually enforce them or stop you from passing a different type.

# def add(a: int, b:int) -> int:
#     return a+b
# This says a and b are expected to be int, and the function is
# expected to return an int

# print(add("3", "5"))
# This still runs, since Python does not enforce type hints, so
# "3"+"5" happens instead, which joins the strings and gives "35"


def multi(a, b):
    return a*b

# One function can call another function. Here area_of_rect() reuses
# the multi() function instead of writing a*b again.
def area_of_rect(length, width):
    return multi(length, width)

print(area_of_rect(10, 5))
