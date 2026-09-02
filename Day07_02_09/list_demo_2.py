# Notes: More List Operations and List Comprehensions
#
# copy
# copy() creates a new, separate list with the same items. Changing
# the copy does not affect the original list.

# a = [1,2, 3]
# b = a.copy() # shallow
# b = a # deep
# Note: b = a does NOT create a copy at all. It just makes b point to
# the same list as a, in memory. Both names refer to one single list.
# So changing b through append, insert etc. will also change a.
# Only b = a.copy() actually creates a separate list.
# print(a)
# print(b)
# b.append(5)
# print(a)
# print(b)


# len(), min(), max(), sum() are built-in functions that work on lists
# print(len([1,2, 3]))     # number of items in the list

# nums = [5, 18, 2, 5]
# print(min(nums))    # smallest value
# print(max(nums))    # largest value
# print(sum(nums))    # total of all values

# in operator
# in checks whether a value exists inside a list, gives True or False

# fruits = ["apple", "banana", "kiwi"]
# print("apple" in fruits)
# print("mango" in fruits)

# # looping through a List
# The simplest way to go through each item in a list

# for f in fruits:
#     print(f)

# Looping using index numbers instead of the items directly, using
# range(len(list)) to generate the valid index positions
# for i in range(len(fruits)):
#     print(i, fruits[i])


# # enumerate
# enumerate() gives both the index and the item together in each round,
# so we do not need range(len(...)) separately

# for i, f in enumerate(fruits):
#     print(i, f)

# fruits = ["apple", "banana", "kiwi", "avocado"]

# Combining a loop with a condition to filter items
# for f in fruits:
#     if f.startswith("a"):
#         print(f)

# sum of numbers
# Adding up all items in a list manually using a loop and a running total

# nums = [5, 18, 2, 5]

# total = 0
# for n in nums:
#     total = total + n
# print(total)

# List comprehensions
# A list comprehension is a short, one line way to build a new list
# from an existing sequence, instead of writing a full for loop with append.
# Syntax

# [new_item_exp for item in itr]

# Square of nums
# The long way, using a normal for loop

# lst = [1, 2, 3, 4, 5, 6]
# res = []
# for x in lst:
#     res.append(x*x)
# print(res)

# The same result written as a list comprehension, in a single line
# print([x*x for x in lst])

# A list comprehension can also include a condition, to filter items
# [new_item_exp for item in itr if cond]

# evens =[]
# for x in range(10):
#     if x%2==0:
#         evens.append(x)
# print(evens)

# Same filtering logic written as a list comprehension
# print([x for x in range(10) if x%2==0])

# A list comprehension can also use if-else to decide what value goes
# in, instead of just filtering items out
# [value_if_true if cond else value_if_False for item in itr]

labels =[]
for x in range(10):
    if x%2==0:
        labels.append("even")
    else:
        labels.append("odd")

print(labels)

# The above loop rewritten as a one line list comprehension using
# a ternary expression (if-else) inside it
labels_res = ["even" if x%2==0 else "odd" for x in range(10) ]
print(labels_res)


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Create a list of 5 numbers and print its length, minimum,
#    maximum and sum using len(), min(), max() and sum().

# 2. Take a list of fruits and check if "mango" is present in it,
#    using the in operator.

# 3. Loop through a list of names and print each name along with
#    its index, using enumerate().

# 4. Create a list a = [1, 2, 3], copy it into b using copy(), then
#    change an item in b and print both a and b to confirm a did
#    not change.

# 5. Create a list a = [1, 2, 3], assign b = a (without copy()), then
#    change an item in b and print both a and b, to see that both
#    changed.

# 6. Write a list comprehension to create a list of cubes (x*x*x)
#    for numbers 1 to 10.

# 7. Write a list comprehension to get all numbers from 1 to 30 that
#    are divisible by 3.

# 8. Write a list comprehension that labels numbers from 1 to 10 as
#    "positive" if greater than 0, otherwise "non-positive".

# 9. Take a list of words and use a list comprehension to create a
#    new list with only the words that start with the letter "s".

# 10. Write a for loop to find the sum of all even numbers between
#     1 and 50, then write the same logic using sum() with a list
#     comprehension.
