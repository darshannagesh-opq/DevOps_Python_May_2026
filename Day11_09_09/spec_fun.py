# Notes: lambda, map(), filter(), zip()

# lambda - temp, one line func
# A lambda is a short, unnamed function written in a single line.
# It is useful for small, throwaway logic, where writing a full def
# function feels unnecessary.

# lambda args: exp
# res = lambda x: x*x
# print(res(5))
# This lambda takes x and returns x*x, same as writing
# def square(x): return x*x, just shorter

# add = lambda a, b: a+b
# print(add(3, 7))
# A lambda can take multiple arguments too, separated by commas

# print((lambda x: "Even" if x%2==0 else "Odd")(11))
# A lambda can be called immediately, right after defining it, by
# adding () with the argument straight after

# map() -> takes a func and an iter
# map() applies a given function to every item in an iterable (like a
# list), and gives back the transformed results.

# map(fun, iter)
# nums = [1, 2, 3, 4, 5, 6]
# def sq(x):
#     return x*x
# map(sq, nums)
# This only creates a map object, it does not print or compute the
# values yet, map() is lazy, the values are only produced when needed

# res = map(lambda x: x*x, nums)
# print(list(res))
# Wrapping it in list() forces map() to actually run on every item
# and gives back the results as a list

# names = ["sam", "ravi", "Asha"]
# result  = map(lambda n: n.upper(), names)
# print(list(result))
# Here the lambda converts each name to uppercase

# map() can also work on two lists together, applying the function
# to matching pairs from each list
# a = [1, 2, 3]
# b = [4, 5, 6]

# res_2 = map(lambda x, y: x * y, a, b)
# print(list(res_2))
# This multiplies a[0]*b[0], a[1]*b[1], a[2]*b[2]

# filter()
# filter() also takes a function and an iterable, but instead of
# transforming every item, it keeps only the items where the function
# returns True.

# nums = [1, 2, 3, 4, 5, 6]

# evens = filter(lambda x: x%2==0, nums)
# print(list(evens))
# Only the numbers where x%2==0 is True are kept

# marks = [23, 45, 67, 88, 65, 89, 75]
# res = filter(lambda m: m>50, marks)
# print(list(res))
# Only keeps marks greater than 50

# zip ()
# zip() combines items from two or more sequences together, pairing
# up items that share the same position.

roll = [1, 2, 3, 4, 5]
names = ["sam", "ravi", "a", "b", "c"]

print(list(zip(roll, names)))
# Pairs each roll number with the name at the same position, as tuples

print(dict(zip(roll, names)))
# Converting the zipped pairs into a dict, using roll numbers as keys
# and names as values


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Write a lambda that takes a number and returns its cube, and
#    call it with 3.

# 2. Write a lambda that takes two numbers and returns the larger one.

# 3. Use map() with a lambda to convert a list of temperatures in
#    Celsius to Fahrenheit (F = C * 9/5 + 32).

# 4. Use map() with a lambda to get the length of each word in a list
#    of words.

# 5. Use filter() with a lambda to get all numbers greater than 10
#    from a list of numbers.

# 6. Use filter() with a lambda to get all words longer than 4
#    characters from a list of words.

# 7. Use zip() to combine a list of student names and a list of their
#    marks into a list of tuples.

# 8. Use zip() and dict() to create a dictionary that maps product
#    names to their prices, from two separate lists.

# 9. Use map() with a lambda to convert a list of strings into a list
#    of integers.

# 10. Combine map() and filter() together, first filter out the even
#     numbers from a list, then use map() to square each of the
#     remaining numbers.
