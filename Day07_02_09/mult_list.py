# Notes: List of Lists (2D Lists / Matrix)
#
# A list of lists is a list where each item is itself another list.
# This is often used to represent a grid or table of values, like a matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix)      # the whole list of lists
# print(matrix[0])   # the first inner list, [1, 2, 3]
# print(matrix[0][0])# first item of the first inner list, 1
# print(matrix[0][1])# second item of the first inner list, 2
# The first [] picks which row (inner list), the second [] picks
# which item inside that row.

# Updating a value inside a nested list, using both index positions
# matrix[0][1] = 10
# print(matrix)

# append() adds a whole new inner list as a new row at the end
# matrix.append([10, 11, 12])
# print(matrix)

# insert(index, list) adds a new row at a specific position
# matrix.insert(1, [100, 111, 222])
# print(matrix)

# del removes an item using its index, it can be used on the outer
# list to delete a whole row, or on an inner list to delete a
# single value inside a row
# del matrix[2]
# print(matrix)
# del matrix[1][0]
# print(matrix)

# Looping through a list of lists needs two loops, an outer loop for
# each row, and an inner loop for each value inside that row
# for r in matrix:
#     for val in r:
#         print(val, end= " ")
#     print()
# end=" " keeps values on the same line, and the empty print() at the
# end of the outer loop moves to a new line after each row

# Copying a list of lists
# copy() only makes a shallow copy. It creates a new outer list, but
# the inner lists inside it are still the same, shared inner lists.
# So changing a value inside a nested list through the copy will
# still affect the original.
a = [[1, 2], [3, 4]]
b = a.copy()
# b[0] = [5, 6]     # this replaces the whole first row in b only,
                    # a stays unaffected, because this changes what
                    # b[0] points to, not the shared inner list itself
b[0][0] = 99        # this changes a value inside the shared inner list,
                    # so it affects both a and b
print(b)
print(a)


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Create a 3x3 matrix using a list of lists and print it.

# 2. Print the item in the second row and third column of the
#    matrix above, using two index positions.

# 3. Change the value in the first row, first column to 100, and
#    print the updated matrix.

# 4. Add a new row [10, 11, 12] to the end of the matrix using append().

# 5. Remove the last row of the matrix using del.

# 6. Use a nested for loop to print every value in the matrix, one
#    value at a time.

# 7. Use a nested for loop to find the sum of all values in the matrix.

# 8. Create a list of lists representing 3 students and their marks
#    in 2 subjects, for example [["Asha", 80, 90], ["Ravi", 70, 60]],
#    then print each student's name with their total marks.

# 9. Create list_a = [[1, 2], [3, 4]], copy it into list_b using
#    copy(), then change a value inside one of the inner lists of
#    list_b, and print both to see that list_a also changed.

# 10. Print the matrix from question 1 in a grid format, using a
#     nested loop and end=" " so each row prints on its own line.
