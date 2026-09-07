# Notes: Built-in Libraries (math, random)
#
# Python comes with many built-in modules already installed, called
# the standard library. We just need to import them, no separate
# installation needed, unlike third party packages.

# import math
# math is a built-in module with common mathematical functions and constants

# print(math.ceil(42.3))    # rounds up to the next whole number, 43
# print(math.floor(42.9))   # rounds down to the previous whole number, 42
# print(math.trunc(42.3))   # simply cuts off the decimal part, no rounding, 42
# print(math.sqrt(4))       # square root
# print(math.log(16, 2))    # logarithm of 16 with base 2
# print(math.exp(2))        # e raised to the power 2
# print(math.pi)            # the value of pi as a constant

import random
# random is a built-in module used to generate random numbers and
# make random selections

# print(random.random())
# gives a random float between 0.0 and 1.0

# print(random.randint(1, 10))
# gives a random whole number between 1 and 10, both included

# print(random.uniform(1.0, 5.0))
# gives a random float between 1.0 and 5.0

lst = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(lst)
# shuffle() rearranges the items of a list randomly, in place,
# it does not return a new list
print(lst)

print(random.choice(lst))
# choice() picks one random item from the list

print(random.sample(lst, 3))
# sample() picks a given number of unique random items from the list,
# without repeating any item
