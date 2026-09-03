# Notes: Tuples in Python
#
# A tuple is similar to a list, but it is immutable, meaning once it
# is created, its items cannot be changed, added or removed.
# It is ordered, so items keep their position, and it allows duplicates.

# immutable, ordered, allow duplicates

my_tuple = (1, 2, 3, 4, 5)

# Accessing items works the same way as lists, using an index
print(my_tuple[0])

# Slicing also works the same way as lists
print(my_tuple[1:4])

t1 = (1, 2)
t2 = (3, 4)
# + joins two tuples together into a new tuple, does not change t1 or t2
print(t1+t2)

# len() gives the number of items in the tuple
print(len(my_tuple))

# Looping through a tuple works the same way as a list
for item in my_tuple:
    print(item)

# count() tells how many times a value appears in the tuple
print(my_tuple.count(3))

# index() gives the position of the first matching value
print(my_tuple.index(3))

# * repeats the tuple's items the given number of times
print(my_tuple * 3)

# A tuple can be converted to a list if it needs to be made mutable
print(list(my_tuple))

# The original tuple stays unchanged, since tuples cannot be modified
print(my_tuple)
