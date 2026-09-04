# Notes: Nested Dictionaries and Dict Comprehensions
#
# A nested dictionary is a dictionary where a value is itself another
# dictionary. This is useful for storing structured data, like a
# student with basic details, marks and contacts all grouped together.

# students = {
#     101: {
#         "basic": {"name": "Kavya", "age": 15, "class": 10},
#         "marks": {"math": 45, "sci": 67},
#         "contacts": ["74757657"],
#     },
#     102: {
#         "basic": {"name": "Riya", "age": 14, "class": 10},
#         "marks": {"math": 65, "sci": 27},
#         "contacts": ["74757657", "65746767"],
#     },
# }
# Here 101 and 102 are roll numbers used as keys, and each value is
# itself a dictionary containing more dictionaries and a list inside it.

# # print(students)
# Accessing a deeply nested value means chaining the keys one after another
# # print(students[102]["marks"]["math"])

# get() can be chained too, and is safer since it does not raise an
# error if a key is missing, it just returns the default value instead
# # print(students.get(102).get("marks").get("social", "Unknown"))

# Adding or updating a value deep inside a nested dictionary works the
# same way as accessing it, just assign a value at the end
# students[102]["marks"]["social"] = 88
# # print(students)


# Adding a whole new nested entry, for a new roll number
# students[103]={
#         "basic": {"name": "Kiran", "age": 14, "class": 10},
#         "marks": {"math": 65, "sci": 57},
#         "contacts": ["74757657"],
#     }

# print(students)

# setdefault(key, default) returns the value for a key if it exists,
# otherwise it creates that key with the given default value.
# Chaining setdefault() like this safely creates missing levels of
# nesting before setting the final value, avoiding errors from
# missing keys.
# students.setdefault(104, {}).setdefault("marks", {})["math"] = 90
# print(students)

# pop(key, default) removes a key from a nested dictionary and returns
# its value, or the default if the key was not found
# students[102]["marks"].pop("sci", "Not found")
# print(students)

# del removes a key directly, but raises an error if the key is missing
# del students[105]


# Looping through a nested dictionary using items() to get both the
# key (roll number) and the value (all the details) together
# for roll, info in students.items():
#     # print(roll)
#     # print(info)
#     name = info["basic"]["name"]
#     math = info["marks"]["math"]
#     print(f"Roll {roll} : {name} - Math: {math}")


# Building a dictionary using a normal for loop
res = {}
for i in range(1, 6):
    res[i] = i*i
print(res)

# Dict comprehension
# The same result written in a single line, similar to a list
# comprehension, but building a dictionary instead
# {key_exp : value_exp for item in itr}
result = {i: i*i for i in range(1, 6) }
print(result)

# A dict comprehension can also include a condition, to filter items
result_even = {i: i*i for i in range(1, 11) if i %2 ==0}
print(result_even)

fruits = ["apple", "mango", "banana", "kiwi"]

# Here each fruit name becomes a key, and its length becomes the value
lengths = {item: len(item)  for item in fruits}
print(lengths)
