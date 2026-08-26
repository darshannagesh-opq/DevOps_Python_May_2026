# Notes: Strings in Python
#
# A string is a sequence of characters. Python treats a string as a
# list of individual characters, which is why indexing and slicing work on it.

#  + , *
# + joins two strings together, this is called concatenation
# * repeats a string a given number of times
# print("OPQ" + "Tech")
# print("abc"*3)

# #  ''' ''' or """ """
# Triple quotes let a string span multiple lines
# s = """I'm learning
# Python String"""
# print(s)

# len()
# len() returns the number of characters in a string, including spaces
# print(len("OPQ tech"))

# Indexing
# OPQtech -> each char has a position (index) -> starting from 0
# O -> 0
# P -> 1

# Python ->
#  [] -> used to access individual characters using their index
# text = "Python"
# print(text[0])
# print(text[2])
# print(text[len(text)-1])   # last character, using length - 1
# # Negative indexing -> -1
# print(text[-1])            # -1 always means the last character

# s = """I'm learning
# # Python String"""
# print(s[3])
# print(s[4])

#  Slicing [start:end]
# Slicing gives a part of the string. It includes the start index
# and stops just before the end index.

# s = "OPQtech"
# OPQ
# print(s[0:2])
# print(s[0:3])

# print(s[3:])    # from index 3 to the end
# print(s[:2])    # from the start up to index 2
# print(s[:])     # the whole string

# String methods for changing case
# name = "OpQ tecH"
# print(name.lower())        # all lowercase
# print(name.upper())        # all uppercase
# print(name.title())        # first letter of each word capitalized
# print(name.capitalize())   # only the first letter of the string capitalized

# strip() removes extra spaces from the start and end of a string
# name = "   OpQ tecH    "
# print(name)
# print(name.strip())

# replace(old, new) swaps out a piece of text with another
# msg = "hello world"
#  replace(old, new)
# print(msg.replace("world", "OPQ"))
# print("banana".replace("a", "*"))

# count() tells how many times something appears in a string
# msg = "hello world"
# print(msg.count("l"))
# print("abracadabra".count("abra"))

# find() gives the index where the text is first found, or -1 if not found
# print(msg.find("llo"))
# print(msg.find("lla"))     # not found, so this gives -1

# index() works like find(), but it raises an error if the text is not found
# print(msg.index("llo"))
# print(msg.index("lla"))    # this line would cause an error

# isspace() checks if a string only contains spaces
# print("     ".isspace())

# String formatting, ways to combine text and variables
# name = "Sam"
# age = 25
# print("Hello "+ name + ", age " + str(age))   # concatenation, needs str() for numbers
# print(f"Hello {name}, age {age}")              # f-string, easier and no need for str()

# User Input - input() -> returns a str
# input() always gives back a string, even if the user types a number
s = input("type something and press enter: ")
print("You typed: ", s)
print("Type of: ", type(s))

# If you need a number from input(), you must convert it yourself using int() or float()
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Sum: ", a+b)


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Take the string "OPQ Technologies" and print its length using len().

# 2. Take the string "Python" and print the first character, the last
#    character (using -1) and the character at index 3.

# 3. Take the string "Hello World" and print just "World" using slicing.

# 4. Take the string "   Data Science   " and print it after removing
#    the extra spaces from both sides using strip().

# 5. Take the string "opq tech" and print it in uppercase, lowercase
#    and title case.

# 6. Count how many times the letter "s" appears in "Mississippi"
#    using count().

# 7. Replace the word "cat" with "dog" in "The cat sat on the mat"
#    using replace().

# 8. Find the index of "World" in "Hello World" using find().

# 9. Take a variable name = "Sam" and city = "Mumbai", and print
#    "Sam lives in Mumbai" using an f-string.

# 10. Ask the user to enter their name using input(), and print
#     "Welcome, <name>!" using an f-string.
