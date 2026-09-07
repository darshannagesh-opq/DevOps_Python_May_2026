# Notes: Using a Module (import)
#
# import brings in another file's (module's) functions and variables
# so we can use them here, without copying the code again.

import support
# This loads the whole support.py module. To use anything from it,
# we prefix it with the module name, like support.function_name

# support.greet("Sam")
print(support.multi(3, 6))
# print("PI= ", support.PI)

# from support import greet, multi
# This imports only specific names from the module, so they can be
# used directly, without the support. prefix

# greet("Sam")
# multi(2, 3)

# from support import *
# This imports everything from the module directly. It is convenient,
# but not recommended for larger projects, since it is not clear
# anymore which module a name came from, and it can accidentally
# overwrite names already used in this file.
# greet("Sam")

# import support as sup
# as lets us give the imported module a shorter or different name (an alias),
# useful when the module name is long or clashes with something else
# sup.greet("Ali")
