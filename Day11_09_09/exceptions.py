# Notes: Exception Handling (try, except, else)
#
# Instead of letting an error crash the program, we can catch it using
# try and except, and handle it gracefully, like showing a friendly
# message instead of a scary error.

# try block
# try:
#     number = int(input("Enter a number: "))
#     print(f"number entered: {number}")
# except ValueError:
#     print("Thats not a valid number")
# Python runs the code inside try first. If an error happens, it jumps
# straight to the matching except block instead of crashing the program.
# Here, if the user types something that is not a number, int()
# raises a ValueError, which gets caught and handled.


# Multiple except blocks handle different error types separately
# try:
#     number = int(input("Enter a number: "))
#     print(f"number entered: {number}")
#     res = 10 /number
#     print(f"Result: {res}")
# except ValueError:
#     print("Thats not a valid number")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# Python checks the except blocks in order, and runs whichever one
# matches the actual error that occurred. Only one except block runs
# per try.

# else block (with try-except)
# An else block after try-except runs only if no error occurred in
# the try block at all. It is a good place for code that depends on
# the try block succeeding completely.
# try:
#     number = int(input("Enter a number: "))
#     res = 10 /number
# except ValueError:
#     print("Thats not a valid number")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print(f"Result: {res}")
# If number and res were both calculated successfully, with no error,
# then the else block runs and prints the result.


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Write a try-except block that asks the user for a number and
#    catches a ValueError if they type something that is not a number.

# 2. Write a try-except block that divides 20 by a number entered by
#    the user, and catches a ZeroDivisionError if they enter 0.

# 3. Combine questions 1 and 2 into one try block with two except
#    blocks, one for ValueError and one for ZeroDivisionError.

# 4. Write a try-except block that accesses an item from a list using
#    an index entered by the user, and catches an IndexError if the
#    index does not exist.

# 5. Write a try-except-else block where the else block prints
#    "Success!" only if no error occurred in the try block.

# 6. Take a dictionary with 3 keys, ask the user to enter a key name,
#    and use try-except to catch a KeyError if the key does not exist.

# 7. Write a try-except block around int(input(...)) that keeps asking
#    the user to enter a number again if they enter invalid input
#    (hint, this will need a loop around the try-except).

# 8. Write a try block with two possible errors, a ValueError and a
#    TypeError, and use a single except that catches both using
#    except (ValueError, TypeError):

# 9. Write a try-except block that catches any error using a general
#    except Exception as e: and prints the error message using e.

# 10. Write a calculator style try-except block that takes two numbers
#     and an operator (+, -, *, /) as input, performs the operation,
#     and handles both ValueError and ZeroDivisionError.
