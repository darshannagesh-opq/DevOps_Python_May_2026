# Notes: pip, venv, and the os Module
#
# Before getting into the os module, here are notes on pip and venv,
# two tools used alongside it for managing Python projects.
#
# pip
# pip is Python's package installer. It downloads and installs third
# party packages (code written by others) so we can use them in our
# own programs, instead of writing everything from scratch.
#
# pip install package_name        installs a package
# pip uninstall package_name       removes a package
# pip list                         shows all installed packages
# pip show package_name            shows details about one package
# pip freeze > requirements.txt    saves all installed packages and
#                                   their versions into a text file
# pip install -r requirements.txt  installs everything listed in
#                                   that file, useful for setting up
#                                   the same packages on another machine
#
# The requirements.txt file in this folder is an example, generated
# using pip freeze, listing packages like boto3, pandas and numpy
# along with their exact versions.
#
# venv
# venv creates a virtual environment, a separate, isolated Python
# setup for one project. Packages installed inside it do not affect
# other projects or the system-wide Python installation. This avoids
# version conflicts between different projects that need different
# versions of the same package.
#
# python -m venv myenv       creates a virtual environment folder
#                            named myenv
# myenv\Scripts\activate     activates it on Windows
# source myenv/bin/activate  activates it on Mac/Linux
# deactivate                 exits the virtual environment
#
# The myenv folder in this directory is an example of a created
# virtual environment. Once activated, any pip install command
# installs packages only inside myenv, not system-wide.


# Notes: The os Module
#
# os is a built-in module used to interact with the operating system,
# such as working with folders, files and paths.

import os

# current working dir
# getcwd() gives the folder Python is currently running from

print("------", os.getcwd())

# change dir
# chdir() changes the current working directory to a new path

# os.chdir("C:\\Users\\darsh\\Desktop")
# print("------", os.getcwd())


# listdir() lists all files and folders inside the current directory
# print(os.listdir())

# mkdir() creates a single new folder
# os.mkdir("test_folder")

# makedirs() creates multiple nested folders at once, even if the
# parent folders do not exist yet
# os.makedirs("parent/child/grandchild")

# rmdir() removes a single empty folder
# os.rmdir("test_folder")

# removedirs() removes nested empty folders, one by one, from the
# innermost folder outward
# os.removedirs("parent/child/grandchild")

# rename() renames a file (or folder), old.txt becomes new.txt
# os.rename("old.txt", "new.txt")

# os.path is a sub-module inside os, used for checking and working
# with file paths specifically

# exists() checks whether a given file or folder path actually exists
# print(os.path.exists("new123.txt"))

# getsize() gives the size of a file in bytes
# print(os.path.getsize("os_mod.py"))


# A practical example: create a folder only if it does not already exist
# if not os.path.exists("logs"):
#     os.mkdir("logs")

# with open("logs/temp_log.txt", "w") as f:
#     f.write("Log file --------")

# os.rename("logs/temp_log.txt", "logs/system_log.txt")
# Renaming works on files inside folders too, just by giving the
# full path

# for file in os.listdir("logs"):
#     print("File inside logs -> ", file)
# Looping through listdir() lets us go through every file inside a
# specific folder


# os.system() runs a shell command directly, similar to subprocess,
# but simpler, it only runs the command and does not let us easily
# capture its output like subprocess.run() does
# os.system("ls")


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Print the current working directory using os.getcwd().

# 2. List all files and folders in the current directory using
#    os.listdir().

# 3. Create a new folder called "practice_dir" using os.mkdir().

# 4. Check if a file called "myfile.txt" exists using os.path.exists(),
#    before trying to open it.

# 5. Create a nested folder structure "a/b/c" in one line using
#    os.makedirs().

# 6. Create a file called "old_name.txt", then rename it to
#    "new_name.txt" using os.rename().

# 7. Print the size of any file in this folder in bytes, using
#    os.path.getsize().

# 8. Write a program that creates a "backup" folder only if it does
#    not already exist, using os.path.exists() and os.mkdir().

# 9. Use os.listdir() combined with a loop to print only files that
#    end with ".txt" from the current folder.

# 10. Remove the "practice_dir" folder created in question 3, using
#     os.rmdir().
