# Notes: Programming Practice
#
# This file solves small, common coding problems using concepts
# already covered: strings, lists, dicts, sets and loops.

#  Count upper case and lower case letters in a string

# text ="Devops Engineer"

# # for i in range(len(text)+1):
# #     if text[i].isUpper():
# The commented attempt above has two problems: range(len(text)+1)
# goes one index too far, and isUpper() is not a real method,
# the correct method is isupper() (all lowercase, no capital U)

# upper = 0
# lower = 0

# for ch in text:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# isupper() and islower() check the case of a single character.
# Characters like spaces are neither, so they are simply skipped
# by this loop.

# print(upper, lower)

# Find the missing number in a seq
# The idea: if numbers from 1 to n were all present, their sum would
# follow a known formula. Comparing that expected sum to the actual
# sum reveals which number is missing.

# seq = [1, 2, 3, 5]
# length_seq = 5
# # 5 * (6) /2 = 15
# excepted_sum = length_seq * (length_seq+1) //2
# This formula, n*(n+1)/2, gives the sum of all numbers from 1 to n
# actual_sum = sum(seq)
# print(excepted_sum-actual_sum)
# The difference between the expected sum and the actual sum is
# exactly the missing number, here 4

# remove duplicates from a list - keeping order
# A set alone can remove duplicates, but it does not preserve the
# original order. This function keeps duplicates out while
# preserving the order items first appeared in.


# def remove_dup(items):
#     res = []
#     seen = set()
#     for item in items:
#         if item not in seen:
#             seen.add(item)
#             res.append(item)
#     return res, seen
# seen is used only to quickly check if we have already added an item
# (checking "in" a set is much faster than checking "in" a list),
# res is the actual ordered result we care about


# print(remove_dup([3, 1, 3, 2, 1, 4]))

# # (3, 1, 2, 4)

# Validate a simple password
# at least 8 chars,  at least one digit, one upper case letter

# def is_valid_pass(pw):
#     if len(pw)< 8: return False
#     has_digit = any(char.isdigit() for char in pw)
#     print(has_digit)
#     has_upper = any(char.isupper() for char in pw)
#     print(has_upper)
#     return has_digit and has_upper
# any() returns True if at least one item in the sequence satisfies
# the condition. Here it checks every character of the password for
# a digit, and separately for an uppercase letter, using a generator
# expression, similar to a list comprehension but without the [].

# print(is_valid_pass("devops123"))
# This has 10 characters and a digit, but no uppercase letter, so it
# returns False

# # Find the most frequent element in a list
# lst = ["error", "info", "error", "error", "info", "warning"]
# # {"error": 3, "info" : 2, "warning": 1}
# def most_frequent(items):
#     counts = {}
#     for item in items:
#         counts[item] = counts.get(item, 0) + 1
# get(item, 0) returns the current count if item exists, or 0 if it's
# new, so we can always add 1 without checking existence separately

#     return max(counts, key=counts.get)
# max() normally compares the items directly, but key=counts.get
# tells it to compare their counts (the dict values) instead, and
# return whichever key had the highest count

# print(most_frequent(lst))

# FizzBuzz
# 1-> 50 , multiples of 3 print Fizz, of 5 print Buzz, both FizzBuzz
#  if -> i % 3 == 0
# elif ->
# A classic beginner problem: check divisibility by both 3 and 5
# first (since 15 is divisible by both), before checking them separately

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Find the sum of all elements in a list without using sum().

# 2. Find the average of a list of numbers.

# 3. Swap the values of two variables without using a third variable.

# 4. Convert a temperature from Celsius to Fahrenheit, and back.

# 5. Check whether a given year is a leap year.

# 6. Find the GCD (greatest common divisor) of two numbers using a loop.

# 7. Find the LCM (least common multiple) of two numbers.

# 8. Capitalize the first letter of every word in a sentence, without
#    using title().

# 9. Count the total number of words in a sentence.

# 10. Merge two dictionaries into a single dictionary.

# 11. Flatten a nested list, e.g. [[1, 2], [3, 4]] -> [1, 2, 3, 4].

# 12. Check if the brackets in a string are balanced,
#     e.g. "(a+b)*(c-d)" is balanced, "(a+b*(c-d)" is not.

# 13. Sort a dictionary by its values, from smallest to largest.

# 14. Find the transpose of a matrix (a list of lists), swapping rows
#     with columns.

# 15. Rotate a list to the left by a given number of positions,
#     e.g. [1, 2, 3, 4, 5] rotated by 2 becomes [3, 4, 5, 1, 2].

# 16. Replace all occurrences of a character in a string with another
#     character, without using replace().

# 17. Check whether a number is a perfect number (the sum of its
#     divisors, excluding itself, equals the number, e.g. 6 = 1+2+3).

# 18. Find the longest word in a sentence.

# 19. Convert a list of tuples, e.g. [("a", 1), ("b", 2)], into a
#     dictionary.

# 20. Count how many numbers in a list are divisible by both 2 and 3.

# 21. Find the intersection and the union of two sets of numbers.

# 22. Generate the first n numbers of the Fibonacci sequence.

# 23. Check whether a string contains only digits, using a loop
#     instead of isdigit().

# 24. Find the index of the maximum value in a list, without using
#     max() or index().

# 25. Convert a string of comma separated numbers, like "3,5,8,2",
#     into a list of integers.
