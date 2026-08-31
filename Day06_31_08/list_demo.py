# Notes: Lists in Python
#
# DS - format to store multiple values in an org way
#
# Python - 4 built in - DS
# List, Tuple, Set, Dict
#
# The problem
# name = "Darshan"
# roll_num = 25
# phone, marks in 5 subjs... , Address, DOB....
# Storing each of these in a separate variable gets messy fast.
# A data structure lets us group related values together under one name.

# List - is an ordered, mutable collection of items
# ordered means items keep the position you placed them in
# mutable means the list can be changed after it is created, items
# can be added, removed or updated
# [....]
# creating lists

# empty_list = []
# # list of names
# students = ["Asha", "Ravi", "Mina"]
# prices = [19.99, 20, 55.99]
# mixed = ["Sam", "1CV15Ec0006", 24, 25, 21,...]
# A list can hold items of different data types together, unlike some
# other languages.

# Accessing items
# Just like strings, list items are accessed using their index,
# starting from 0. Negative indexing works too, -1 is the last item.
# students = ["Asha", "Ravi", "Mina"]
# print(students[0])
# print(students[1])
# print(students[-1])

# list()
# list() converts another sequence, like a string or a range, into a list

# name = "Asha"
# print(list(name))
# # ['A', 's', 'h', 'a']
# Each character of the string becomes a separate item in the list

# r = range(1, 6)
# print(list(r))
# range() by itself does not show numbers, converting it to a list does

# sentence = "python is fun"
# print(list(sentence))
# print(list(sentence.split()))
# split() breaks a string into a list of words, using space as the
# default separator, this is different from list(sentence) which
# breaks it into individual characters

# Slicing works on lists the same way it works on strings
# list[start:stop:step]

# a = [0, 1, 2, 3, 4, 5, 6]
# print(a[2:5])     # items from index 2 up to, but not including, index 5
# print(a[:3])      # from the start up to index 3
# print(a[3:])      # from index 3 to the end
# print(a[::2])     # every second item, using a step of 2
# print(a[::-1])    # the whole list reversed, step of -1
# print(a[5:1:-1])  # from index 5 down to index 2, moving backwards

# Since lists are mutable, an item can be changed by assigning a new
# value to its index
# students = ["Asha", "Ravi", "Mina"]
# print(students)
# students[1] = "Riya"
# print(students)

# append() adds a single item to the end of the list
# students.append("Sam")
# print(students)

# extend() adds multiple items from another list, one by one, to the end
# students.extend(["Ram", "Robin"])
# print(students)

# insert(index, item) places an item at a specific position, pushing
# the rest of the items forward
# students.insert(2, "kavya")
# print(students)

# remove(item) deletes the first matching item from the list, by its value
# students.remove("Ravi")
# print(students)

# pop() removes and returns the last item, or the item at a given
# index if one is passed
# nums = [10, 20, 30, 40, 50]
# nums.pop()      # removes the last item, 50
# nums.pop(1)     # removes the item at index 1, 20
# # nums.pop(10)  # this fails, there is no item at index 10
# print(nums)


# remove() only deletes the first occurrence of a value, if the same
# value appears multiple times, a loop is needed to remove all of them
# nums =[2, 3, 4, 2, 2,4, 5]
# # nums.remove(2)
# # print(nums)

# while 2 in nums:
#     nums.remove(2)
# This keeps removing 2 from the list until no more 2s are left

# print(nums)


students = ["Asha", "Ravi", "Mina"]
# clear() empties the list completely, leaving an empty list behind
# students.clear()
# print(students)

# index(item) returns the position of the first matching item
# print(students.index("Ravi"))

# index() can also take a start and end range to search within
# nums =[2, 3, 4, 2, 2,4, 5]
# print(nums.index(4, 2, 7))

# count(item) tells how many times a value appears in the list
# print(nums.count(2))
marks = [20, 50, 40, 80, 70]
print(marks)

# sort() arranges the list in place, from smallest to largest by default
marks.sort()
# print(marks)
# reverse=True sorts from largest to smallest
# marks.sort(reverse=True)
# print(marks)
students.sort()
print(students)

# sorted() is different from sort(), it does not change the original
# list, instead it returns a new sorted list
# new_list =sorted(marks)
# print(marks)

# print(new_list)

# reverse() flips the order of the list in place, it does not sort it,
# it just reverses whatever order the items are already in
marks.reverse()
print(marks)
