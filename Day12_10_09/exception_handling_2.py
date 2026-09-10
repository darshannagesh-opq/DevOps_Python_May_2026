# Notes: Exception Handling Part 2 (finally, raise)

# # finally
# f = None
# try:
#     f = open("example.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     if f is not None:
#         f.close()
#         print("Closed")
# finally always runs, no matter what happens in try, whether an
# error occurred or not. It is commonly used for cleanup work, like
# closing a file, so the file gets closed even if reading it failed.
# f is checked for None here because if open() itself failed, f would
# never have been assigned a real file, so f.close() would fail too.


# raise lets us manually trigger our own error, when something in
# our program's logic does not make sense, even if Python itself
# would not normally raise an error for it.
def check_age(age):
    if age<0:
        raise ValueError("Age cannot -ve")
    ticket_price = 500/age
    return ticket_price
# A negative age is not something Python checks for automatically,
# but it does not make sense for our program, so we raise a
# ValueError ourselves with a custom message.
# If age is 0, 500/age causes a real ZeroDivisionError on its own,
# we do not need to raise that one manually.

try:
    user_age = int(input("Enter age: "))
    res = check_age(user_age)
except ValueError as v:
    print(v)
# "as v" stores the error object in v, so print(v) shows the actual
# error message, here it could be either int()'s own error message,
# or our own "Age cannot -ve" message from raise
except ZeroDivisionError:
    print("Age cannot be zero ")
else:
    print("Ticket price = ", res)
finally:
    print("Program finished")
# finally runs here regardless of whether check_age() succeeded,
# raised a ValueError, or raised a ZeroDivisionError


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Write a try-except-finally block that opens a file that does not
#    exist, catches the FileNotFoundError, and prints "Done" in the
#    finally block regardless.

# 2. Write a function check_marks(marks) that raises a ValueError if
#    marks is less than 0 or greater than 100, otherwise returns the
#    marks.

# 3. Write a function check_positive(n) that raises a ValueError with
#    the message "Number must be positive" if n is negative.

# 4. Call the function from question 2 inside a try-except block, and
#    print the error message if a ValueError is raised.

# 5. Write a function divide(a, b) that raises a ZeroDivisionError
#    with a custom message "Cannot divide by zero" if b is 0.

# 6. Write a try-except-else-finally block around the divide() function
#    from question 5, printing the result in the else block, and
#    "Operation complete" in the finally block.

# 7. Write a function that raises a custom ValueError if a password
#    entered is shorter than 6 characters.

# 8. Combine raise with a loop, keep asking the user to enter age
#    until a valid non-negative age is entered, raising and catching
#    a ValueError for invalid entries.

# 9. Write a try-finally block (without except) that always prints
#    "Cleanup done" after the try block, whether or not an error occurs.

# 10. Write a function check_username(name) that raises a ValueError
#     if the name contains any spaces, then test it inside a
#     try-except-finally block.
