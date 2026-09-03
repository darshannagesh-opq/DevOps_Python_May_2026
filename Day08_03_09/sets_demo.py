# Notes: Sets in Python
#
# A set stores unique values, duplicates are automatically removed.
# A set is also unordered, so the items do not keep a fixed position,
# and cannot be accessed using an index like a list.

#  unique, unordered

# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# add() adds a single item to the set
# my_set.add(6)
# print(my_set)

# pop() removes and returns a random item from the set, since a set
# has no defined order, we cannot control which item gets removed
# value = my_set.pop()
# print(my_set)
# print(value)

# discard(value) removes a specific value if it exists
# my_set.discard(3)
# print(my_set)

# discard() does not raise an error even if the value is not present
# my_set.discard(8)
# print(my_set)

# Looping through a set, order is not guaranteed
# for val in my_set:
#     print(val)

# Sets support mathematical operations, similar to sets in math

# 1. Union - | or .union()
# Union combines all items from both sets, without duplicates

a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7}

# u1 = a|b
# print(u1)

# u2 = a.union(b)
# print(u2)

# intersection - & or .intersection()
# Intersection gives only the items that are common to both sets

# i1 =  a&b
# print(i1)

# Difference > - or .difference()
# a - b gives items that are in a but not in b

# print(a-b)
# print(b-a)

#  symmetric diff - ^ or symmetric_difference()
# Symmetric difference gives items that are in either set, but not in both
# print(a^b)

# A common practical use of sets is removing duplicates from a list
# nums = [1, 2, 3, 2, 2, 4, 3, 5, 5, 1]

# uq_set = set(nums)
# print(uq_set)
# Converting back to a list if the result needs to be a list again
# uq_list = list(uq_set)
# print(uq_list)
# Note: converting to a set and back to a list may not keep the
# original order of items, since sets are unordered
