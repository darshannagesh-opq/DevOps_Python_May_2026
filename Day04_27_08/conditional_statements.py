# Notes: Conditional Statements in Python
#
# Conditional statements allow us to make decisions in code.
# Based on whether a condition is True or False, different code runs.

# Indentation - leaving some space
# Python uses indentation, not curly brackets, to decide which lines
# belong inside a block. All lines inside an if block must be indented
# by the same amount, usually 4 spaces.

# if, elif, else
# if marks > 90 -> A+

# if condition:
    # code to run when cond is T

# n = int(input("Enter a number: "))

# if n>0:
#     print("+ve number")
#     print("Inside the if block")

# print("Outside the if block")
# This last line is not indented, so it always runs, whether the
# condition was True or False.


# if-else lets us run one block when the condition is True and
# another block when it is False

# if condition:
    # code to run when cond is T
# else:
    # code to run when cond is F


# n = int(input("Enter a number: "))

# if n>0:
#     print("+ve number")
#     print("Inside the if block")
# else:
#     print("Not a +ve number")

# print("Outside the if block")

# if + elif + else
# elif lets us check multiple conditions one after another.
# Python checks them in order and runs the first one that is True.
# If none of them are True, the else block runs.

# if condition1:
    # code to run when cond is T
# elif cond2:
    #  runs if cond1 is F and cond 2 is T
# else:
    # code to run when cond is F

# n = int(input("Enter a number: "))

# if n>0:
#     print("+ve number")
# elif n==0:
#     print("Number is zero")
# else:
#     print("-ve number")

# n = int(input("Enter a number: "))

# Checking even or odd using modulo
# if n%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# take age input
# age < 13 - child
# 13-19 - teenager
# otherwise -> Adult

# if + nested if + else
# A nested if is an if statement written inside another if or else block.
# It is used when a decision depends on more than one condition, checked in stages.

# age = int(input("Enter age: "))

# if age < 13:
#     print("Child")
# else:
#     if age <= 19:
#         print("Teenager")
#     else:
#         print("Adult")


# Another nested if example, this time with two separate conditions,
# age and membership, checked together

# age = int(input("Enter age: "))
# member = False

# if age> 18:
#     if member:
#         print("Ticket price is 12/-")
#     else:
#         print("Ticket price is 20/-")
# else:
#     if member:
#         print("Ticket price is 8/-")
#     else:
#         print("Ticket price is 10/-")


# one line if else
# This is called a ternary expression. It is a shorter way to write
# a simple if-else in a single line.

# value_if_true if cond else value_if_False
# x = -10

# result = "+ve" if x>0 else "-ve"
# print(result)

# print("Even" if 11 % 2==0 else "Odd")

# Ternary expressions can be chained to act like if-elif-else
# age = int(input("Enter age: "))
# print("Child" if age< 13 else "Teenager" if age<=19 else "Adult")


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Take a number as input and print whether it is positive, negative
#    or zero, using if, elif and else.

# 2. Take a number as input and print "Even" or "Odd" using if-else.

# 3. Take three numbers as input and print the greatest of the three,
#    using if, elif and else.

# 4. Take a year as input and print whether it is a leap year or not.
#    A year is a leap year if it is divisible by 4.

# 5. Take marks as input and print the grade using the following rule:
#    marks >= 90 -> A+, marks >= 75 -> A, marks >= 50 -> B, otherwise -> Fail

# 6. Take age as input and print "Child" if age is below 13,
#    "Teenager" if age is between 13 and 19, otherwise print "Adult".
#    Use nested if-else for this.

# 7. Take a number as input and print whether it is divisible by both
#    3 and 5, using the and operator inside an if condition.

# 8. Take a character as input and print whether it is a vowel or a
#    consonant, using if-elif-else.

# 9. Rewrite question 2 (Even or Odd) using a one line if-else
#    (ternary expression).

# 10. Take the price of an item and a membership status (True/False)
#     as input, and print the final price after a 10 percent discount
#     if the person is a member, otherwise print the price unchanged.
