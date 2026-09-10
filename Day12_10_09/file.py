# Notes: File Handling in Python

# a container used to store data on disk
#  name, type, size, & loc
# A file is a container on disk where data is stored permanently,
# unlike a variable, which is lost once the program ends.

#  Human readable, Binary Files
# Text files (like .txt) store human readable characters.
# Binary files (like .png, .jpg) store raw data as bytes, not
# readable as plain text.

# open("path", "mode")
# open() is used to access a file. "path" is the file's location,
# "mode" tells Python what we intend to do with it, read, write, etc.

# read the file

# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()
# "r" mode opens a file for reading. read() reads the entire content
# of the file as one string. close() releases the file once done,
# it is important to always close a file after opening it.

# f = open("demo.txt", "r")
# data = f.read(5)
# print(data)
# f.close()
# Passing a number to read() reads only that many characters,
# starting from the current cursor position

# f = open("demo.txt", "r")
# print(f.readline())
# print(f.readline())
# f.close()
# readline() reads just one line at a time, moving to the next line
# each time it is called

# f = open("demo.txt", "r")
# print(f.readlines())
# f.close()
# readlines() reads the whole file and gives back a list, where each
# item is one line of the file

# f = open("sample.txt", "w")
# f.write("Hello! \n")
# f.write("Welcome!")
# f.close()
# "w" mode opens a file for writing. If the file already has content,
# it is erased completely and replaced with whatever we write now.

# f = open("sample.txt", "w")
# f.write("Bye \n")
# f.write("Welcome!")
# f.close()
# Opening in "w" mode again erases the previous content ("Hello!
# Welcome!") and replaces it with this new content

# f = open("sample.txt", "w")
# lines = ["line1 \n", "line2 \n", "line 3 \n"]
# f.writelines(lines)
# f.close()
# writelines() writes a list of strings to the file, one after another.
# It does not add new lines automatically, each string must include
# its own \n if a new line is needed.

# seek() - move the file cursor
# The file cursor marks the current reading/writing position in the
# file. seek(position) moves it to a specific byte position.

# f = open("demo.txt", "r")
# f.seek(7)
# data = f.read(5)
# print(data)
# f.close()
# This skips the first 7 characters, then reads the next 5


# tell()
# tell() tells us the current position of the file cursor
# f = open("demo.txt", "r")
# print(f.tell())    # 0, cursor is at the very start
# data = f.read(5)
# print(f.tell())    # 5, cursor has moved forward by 5 characters
# print(data)
# f.close()

# with
# Using "with" automatically closes the file once the block finishes,
# even if an error occurs inside it, so we do not need to call
# close() ourselves. This is the recommended way to work with files.

# with open("demo.txt", "r") as f:
#     print(f.read())

# r
# "r" mode requires the file to already exist, otherwise it raises
# an error

# f = open("demo123.txt", "r")
# data = f.read(5)
# print(data)
# f.close()
# This fails with FileNotFoundError, since demo123.txt does not exist

# w
# "w" mode creates the file if it does not exist, or erases it
# completely if it does

# f = open("sample.txt", "w")
# f.write("Bye \n")
# f.write("Welcome!")
# # data = f.read(5)
# # print(data)
# f.close()
# Note: a file opened in "w" mode cannot be read, that is why the
# read() lines above are commented out, they would raise an error

# append
# "a" mode adds new content to the end of the file, without erasing
# what was already there

# f = open("sample.txt", "a")
# f.write("New line")
# f.close()

# r+ -> read + write
# "r+" allows both reading and writing, but the file must already exist

# f = open("demo.txt", "r+")
# f.write("\nStart new")
# print(f.read())
# f.close()
# Writing moves the cursor forward, so read() after write() only
# reads whatever comes after the new cursor position, not the
# whole file from the start

# w+ => write + read
# "w+" also allows both reading and writing, but like plain "w",
# it erases the file's existing content first

# f = open("sample.txt", "w+")
# f.write("Start new")
# print(f.read())
# f.close()
# print(f.read()) here gives an empty result, because the cursor is
# sitting right after the text we just wrote, at the end of the file,
# there is nothing left after it to read

# a+
# "a+" allows both appending and reading, without erasing existing content

# f = open("sample.txt", "a+")
# f.write("New line")
# print(f.tell())   # cursor is now at the end, after the new text
# f.seek(0)         # move the cursor back to the start to read from the beginning
# print(f.read())
# f.close()

# Working with binary files, like images, needs "rb" (read binary)
# and "wb" (write binary) modes instead of plain "r" and "w"

# with open("download.png", "rb") as f:
#     data =  f.read()
#     print(len(data))
# This reads the image as raw bytes, and len(data) gives the file
# size in bytes

# with open("download.png", "rb") as f:
#     data =  f.read()
#     print(len(data))

# with open("copy.png", "wb") as d:
#     d.write(data)
# This writes the same bytes into a new file, copy.png, effectively
# copying the image

# from datetime import datetime

# with open("logs.txt", "a") as f:
#     f.write(f"User logged in at {datetime.now()}\n")
# A practical use of append mode, adding a new log entry with a
# timestamp each time this code runs, without erasing previous logs

# A practical example: reading a simple config file line by line,
# where each line is in the format key=value
with open("config.txt", "r") as f:
    # print(f)
    for line in f:
        key, value = line.strip().split("=")
        print(key, "=", value)
# Looping directly over f reads one line at a time. strip() removes
# the trailing newline and extra spaces, and split("=") breaks the
# line into the key and the value around the = sign


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Create a text file named notes.txt and write 3 lines into it
#    using write(), with \n between each line.

# 2. Open notes.txt and read its entire content using read().

# 3. Open notes.txt and read only the first line using readline().

# 4. Open notes.txt and read all its lines into a list using readlines().

# 5. Append a new line to notes.txt without erasing the existing content,
#    using "a" mode.

# 6. Use seek() to move the cursor to position 5 in notes.txt, then
#    read the next 10 characters.

# 7. Rewrite question 1 to 5 using "with open(...) as f:" instead of
#    manually calling close().

# 8. Create a config file with 3 key=value pairs (like config.txt in
#    this folder), then write code to read it and print each key and
#    value separately.

# 9. Write a small program that copies the content of one text file
#    into another text file.

# 10. Write a program that appends the current date and time to a
#     log file called activity_log.txt every time it runs, using the
#     datetime module.
