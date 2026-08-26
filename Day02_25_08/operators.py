# Notes: Operators in Python
#
# An operator performs an action on values, called operands.
# The three types covered here are Arithmetic, Comparison and Logical.

# Arithmetic, Comparison, Logical

# Addition +
# print(2+3)
# print(2.5+3.5)
# print(2+3.5)   # int + float gives a float

# Strings can be joined with +, this is called concatenation
# print("Good"+"Morning")
# # print(2+"3")  # not allowed, cannot add a number and a string directly
# print(2+True)   # bool acts like a number here, True is 1, so this is 2+1

# Subtraction -
# print(5-2)
# print(5.1-2.4)
# print(True-False)   # True is 1, False is 0, so this is 1-0

# Subtraction does not work on strings
# print("Good"-"Morning")

# Multiplication *
# print(2*3)
# print(2.5*3)
# print("abc"*3)      # a string times a number repeats the string
# # print("abc"*3.5)  # not allowed, cannot multiply a string by a float

# True division /
# Division always gives a float result, even if the numbers divide evenly

# print(4/2)
# print(5/2)

# # Floor division //
# Floor division divides and drops the decimal part, gives a whole number down

# print(7//2)
# print(4//2)
# print(2.5//1.2)

# modulo %
# Modulo gives the remainder left after division

# print(7%2)
# print(5.5%2)

# Exp **
# ** raises a number to a power, pow() does the same thing
# print(3**2)
# print(pow(3, 2))

# abs()
# abs() removes the negative sign and returns the positive value
# print(abs(-35))
# print(abs(10))
# print(abs(-3.1))

# round()
# round() rounds a number to the nearest whole number by default
# a second argument tells it how many decimal places to keep
# print(round(5.6789))
# print(round(5.6789, 2))


# Which data types can be used together with arithmetic operators:
# int - int, float - float, bool - int, string - string, int - float
# string - number combinations are not allowed

# Comparison operators compare two values and always give True or False

# # ==  checks if two values are equal
# print(1==1)
# print(1.0==1)          # int and float can still be equal in value
# print("sam"=="Sam")    # strings are case sensitive, so this is False
# print(True==1)         # True equals 1

# # !=  checks if two values are not equal

# print(1 != 1)
# print(1 != 2)

# >, <, >=, <=  compare size
# print(3>2)
# print(3<2)
# print(3>=3)
# print(2<=2.0)

# Comparing a number with a string is not allowed
# print(1<"A")

# Logical operators combine multiple conditions: and, or, not

# and -> both conditions must be True for the result to be True
# T and T - T
# F and T - F
# T and F - F
# F and F - F

# or -> at least one condition must be True for the result to be True
# T or T - T
# F or T - T
# T or F - T
# F or F - F

# not -> reverses the bool value
# not T -> False
# not F -> True

# print(2+3*4)
# 20, 14

# PEMDAS decides the order in which an expression is calculated
# Python follows a similar order, from highest to lowest:

# ()          brackets first
# **          power
# *, /, //, % multiplication, division, floor division, modulo
# +, -        addition, subtraction
# comp        comparison, ==, !=, >, <, >=, <=
# not         logical not
# and         logical and
# or          logical or

print(2+3*4)          # * happens before +, so this is 2 + 12
print(5+2*3**2)        # ** happens first, then *, then +
print(10-2+5)          # same precedence, so left to right
print(10-(2+5))        # brackets happen first
print((5+2)*3)         # brackets happen first

print(10>5 and 3*2 == 6)
#  10>5 and 6==6
# True and True

print(5+3>6 or not 2==2)
# 8>6 or not 2==2
# T or not T
# T or F
# T

print(5>3 and 10>5)
print(2==2 or 2==3)
print((100>50) or (20>90 and 5<1))


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Print the result of 15 + 4 * 2.

# 2. Print the result of (15 + 4) * 2, and compare it with question 1.

# 3. Print the quotient and remainder of 29 divided by 4,
#    using floor division and modulo.

# 4. Print 2 raised to the power 10, using both ** and pow().

# 5. Print the absolute value of -48 and round 7.4567 to 2 decimal places.

# 6. Print whether 15 is equal to 15.0.

# 7. Print whether 20 is greater than 15 and 15 is greater than 10,
#    using the and operator in one line.

# 8. Print whether 5 is greater than 10 or 3 is less than 8,
#    using the or operator in one line.

# 9. Print the result of not(5==5).

# 10. Print the result of 3 + 4 * 2 - 6 / 2, and work out by hand
#     why Python gives that answer using PEMDAS.

