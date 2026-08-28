# Notes: for Loop in Python
#
# A loop repeats a block of code multiple times, instead of writing
# the same line again and again.

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# The five lines above do the same thing five times. A loop lets us
# do this in just two lines.

# loop -> repeats a block of code multiple times
#  for - in seq, while
# Python has two kinds of loops: for (used when we loop over a sequence
# or a known number of times) and while (used when we loop as long as
# a condition is True).

# for var in seq:
    # code - runs for each item in seq
# On each round, var takes the next value from seq, and the indented
# code runs once for that value.

# range() -> generates a seq of ints.
# range() does not create a list of numbers directly, it generates
# them one at a time, which makes it efficient for looping.

# range(end) -> 0 -> end -1
# range(start, end) -> start -> end -1
# range(start, end, step) -> start -> end -1 -> 1, 10, 2
# In all cases, the end value is never included, it stops one before it.

# for i in range(5):
#     print(i)
# This prints 0, 1, 2, 3, 4 (five numbers, not including 5)


# multi table 1 to 10 - user input

# n= int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n, "x" , i, "=", n*i)
# This loop runs with i from 1 to 10, printing the multiplication table of n


# Using if inside a for loop to filter values
# for i in range(1, 11):
#     if i%2 != 0:
#         print(i)
# This prints only the odd numbers between 1 and 10


# Using the step value in range() to skip numbers
# for i in range(1, 11, 2):
#     print(i)
# This starts at 1 and adds 2 each time, so it prints 1, 3, 5, 7, 9

# 1, 2, 3,4, 5, 6 = 6
# 1, 1
# 1, 2
# 1, 3
# 1, 4

# 1, 6

# 2, 1
# 2, 2

# 6, 6

# Nested loops - a loop written inside another loop
# The inner loop completes all its rounds for every single round of
# the outer loop. This is useful for pairs, grids and combinations,
# like rolling two dice together.

# for i in range(1, 7):
#     for j in range(1, 7):
#         print(i, j)
# This prints every possible pair from two dice, 36 pairs in total

# Adding a condition inside the nested loop to filter specific pairs
# target = 5
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j ==target:
#             print(i, j)
# This prints only the pairs whose sum is equal to target

# Counting how many pairs match a condition, and using that count
# to calculate a probability
# target = 5
# total = 36
# count = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == target:
#             count = count + 1

# prob =  (count / total)* 100
# print(f"pairs:{count}, Prob: {prob:.2f}%")

# Same idea extended to three nested loops, for three dice instead of two
# target = 5
# total = 216
# count = 0
# for i in range(1, 7):
#     for j in range(1, 7):
#         for k in range(1, 7):
#             if i + j + k == target:
#                 count = count + 1

# prob =  (count / total)* 100
# print(f"pairs:{count}, Prob: {prob:.2f}%")

# Continue
# continue skips the rest of the code for that round only, and moves
# on to the next round of the loop. It does not stop the loop.

# for i in range(1, 11):
#     if i % 2 ==0:
#         continue
#     print("Odd numbers")
# When i is even, continue skips the print line for that round



# for i in range(1, 11):
#     if i  ==5:
#         continue
#     print(i)
# This prints all numbers from 1 to 10 except 5

# break stops the loop completely, even if there were more rounds left.
# An else block on a for loop runs only if the loop finished normally,
# without hitting a break.

for i in range(1, 10):
    if i == 20:
        print("Found")
        break
else:
    print("Not found")
# Since 20 never appears in range(1, 10), break never runs,
# so the loop finishes normally and the else block prints "Not found"


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Print numbers from 1 to 10 using a for loop and range().

# 2. Print all even numbers between 1 and 20 using a for loop and if.

# 3. Take a number as input and print its multiplication table
#    from 1 to 10.

# 4. Find the sum of all numbers from 1 to 100 using a for loop.

# 5. Print numbers from 10 down to 1 using range() with a negative step.

# 6. Take a number as input and check whether it is prime, by trying
#    to divide it by all numbers from 2 up to the number minus 1.

# 7. Print a multiplication grid for numbers 1 to 5, using a nested
#    for loop (print i * j for every combination of i and j).

# 8. Print all numbers from 1 to 30 except multiples of 3, using
#    continue inside a for loop.

# 9. Search for a number in range(1, 50) using break, and print
#    "Found" if it exists, otherwise use the for-else to print
#    "Not found".

# 10. Count how many numbers between 1 and 50 are divisible by both
#     4 and 6, using a for loop and if.
