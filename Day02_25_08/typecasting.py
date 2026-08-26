# Notes: Type Casting in Python
#
# Type casting means converting a value from one data type to another.
# The main functions used for this are int(), float(), str() and bool().

#  int(), float(), str(), bool()

# int() converts a value to a whole number
# print(int(3.14))          # drops the decimal part, does not round, gives 3
# print(int(True))          # True becomes 1, False becomes 0
# print(int("123"), type(int("123")))   # a string of digits can be converted to int
# print(int("123abc"))      # this fails, a string with letters cannot become an int

# float() converts a value to a decimal number
# print(float(3))
# print(float(False))       # False becomes 0.0
# print(float("10.5"))      # a string that looks like a number can be converted

# str() converts a value to text
# print(str(123), type(str(123)))
# print(str(3.14))
# print(str(True))

# bool() converts a value to True or False
# Numbers that are 0 become False, any other number becomes True
# print(bool(0))
# print(bool(123))
# print(bool(0.0))
# print(bool(0.0000001))    # very small but not zero, so this is True

# Strings follow a similar rule, empty string is False, any other text is True
# print(bool(""))
# print(bool(" "))          # a space is still a character, so this is True
# print(bool("0"))          # this is text "0", not the number 0, so this is True

# Type casting can be combined, working from the inside out
# print(int(float("31.4")))   # string to float first, then float to int
# print(float(int(3.99)))     # int drops the decimal first, then converts to float

# int("31.4")
# this fails, int() cannot directly convert a decimal looking string
# you must convert it to float first, then to int

# This line will cause an error
# int() cannot convert a string that has a comma in it, commas are not digits
print(int("12,345"))


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Convert the float 9.99 to an int and print it. Note what happens
#    to the decimal part.

# 2. Convert the string "45" to an int, then print its type to confirm.

# 3. Convert the number 100 to a string and join it with the text
#    " runs scored" using +.

# 4. Convert the boolean False to an int and to a float, and print both.

# 5. Print bool("") and bool("False") and note that both are strings,
#    but they give different results.

# 6. Take the string "7.8" and convert it directly to an int using
#    two steps, string to float, then float to int.

# 7. Print the type of int("50") and the type of "50" to see the difference.

# 8. Convert the float 3.0 to a string and print its type.

# 9. Print bool(-5) and bool(0) and note which one is True.

# 10. Try converting the string "twenty" to an int using int("twenty")
#     and note what kind of error Python gives.

