# Notes: Dictionaries in Python
#
# A dictionary stores data as key - value pairs, instead of just a
# plain sequence of values like a list.

# key - value pairs

# var_name = { key : value}

# list - ordered data, dict - labelled data
# In a list, you access items using their position (index).
# In a dict, you access items using a meaningful label (key) instead.

# students = {
#     "name" : "Sam",
#     "age" : 25,
#     "phone" : 1234534
# }
# print(students)

# # keys must be unique
# If the same key is written more than once, the last value overwrites
# the earlier ones, only one value is kept per key.

# d = {
#     1: "Asha", 2:"Sam", 1:"ravi"
# }

# print(d)
# Here key 1 appears twice, so "ravi" overwrites "Asha", and the
# dict ends up with only two keys, 1 and 2

# students = {
#     "name" : "Sam",
#     "age" : 25,
#     "phone" : 1234534
# }

# Accessing a value using its key, inside square brackets
# print(students["age"])
# print(students["dob"])   # this fails, "dob" is not a key in students

# .get()
# get() also fetches a value by key, but it does not raise an error
# if the key is missing, it returns None instead

# print(students.get("dob"))
# get() can also take a default value to return when the key is missing
# print(students.get("dob", "Not found"))

# Updating an existing key, or adding a new key, uses the same syntax
# students["name"] = "Neha"
# print(students)
# students["dob"] = "10-07-111"
# print(students)

# update() adds multiple new key-value pairs at once, or updates
# existing ones, using another dict
# students.update({"Address": "Blore", "Pincode":543123})
# print(students)

# d = {
#     1: "Asha", 2:"Sam"
# }

# pop(key) removes a key and returns its value
# value = d.pop(2)
# print(d)
# print(value)

# pop() can also take a default value, returned when the key is not found,
# so it does not raise an error
# value = d.pop(4, "Not Found")
# print(d)
# print(value)

# del removes a key directly, but it raises an error if the key does not exist
# del d[5]
# print(d)

# popitem() removes and returns the last inserted key-value pair
# d.popitem()
# print(d)

# clear() empties the dictionary completely
# d.clear()
# print(d)


# students = {
#     "name" : "Sam",
#     "age" : 25,
#     "phone" : 1234534
# }

# dict.keys()
# keys() gives all the keys, values() gives all the values, and
# items() gives key-value pairs together
# print(students.keys())
# print(students.values())
# print(students.items())

# Looping through just the keys
# for key in students.keys():
#     print(key)


# Looping through both keys and values together, using items()
# for key, value in students.items():
#     print(key, value)


a = {"x":1, "y":2}
b = {"y":20, "z":22}
# update() merges another dict into this one. If a key exists in both,
# the value from the dict passed in (b) overwrites the original (a)
# a.update(b)
# print(a)
# print(b)

# **a, **b -> new dict
# ** unpacks the key-value pairs of a dict. Using it inside {} combines
# both dicts into a brand new dict, without changing a or b.
# If the same key exists in both, the later one (b here) wins.
merged = {**a, **b}
print(merged)
