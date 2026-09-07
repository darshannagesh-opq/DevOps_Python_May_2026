# Notes: Creating a Module
#
# A module is just a normal Python file whose functions and variables
# can be reused in another file, by importing it. This file, support.py,
# is the module, and app.py imports and uses it.

def greet(name):
    print("Hello", name)
# print("Running support ....")
def multi(a, b):
    return a*b

# print("testing multi:")
# print(multi(10, 20))

PI = 3.14159

# __name__
# Every Python file has a built-in variable called __name__.
# When a file is run directly, __name__ is set to "__main__".
# When a file is imported into another file instead, __name__ is set
# to the module's own name, not "__main__".

if __name__ == "__main__":
    print("testing multi:")
    print(multi(10, 20))
# Because of this check, the two lines above only run when support.py
# is run directly (python support.py). They do NOT run when support.py
# is imported by app.py, which keeps import-only code separate from
# testing/demo code.
