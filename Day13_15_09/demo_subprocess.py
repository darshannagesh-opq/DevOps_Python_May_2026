# Notes: The subprocess Module
#
# subprocess lets a Python program run other programs or terminal
# commands, and see their output. This is how Python can trigger
# system level tasks, like running shell commands, from inside code.

import subprocess

# subprocess.run(command, shell=True, check=False)
# subprocess.run() runs a command and waits for it to finish.
# shell=True means the command is run through the system shell
# (cmd on Windows, bash on Mac/Linux), which lets us use normal
# shell syntax like &&, |, and redirects (>).
# check=False means Python will not raise an error even if the
# command itself fails, check=True would raise one on failure.

# subprocess.run("echo Hello from Python!", shell=True, check=False)
# Mac/Linux

# On Mac/Linux, a command can also be passed as a list of separate
# words instead of one string, which avoids depending on shell=True
# subprocess.run(["echo", "Hello from python!"], check=False)

# subprocess.run("dir", shell=True, check=False)
# subprocess.run("mkdir test_folder", shell=True, check=False)
# subprocess.run("echo Done!", shell=True, check=False)
# subprocess.run("dir", shell=True, check=False)
# Each run() call is a separate command, one after another. dir lists
# files, mkdir creates a folder, echo prints text.

# capture_output=True and text=True let us capture the command's
# output inside Python, instead of it just printing to the terminal
# result = subprocess.run(
#     "echo Hello", capture_output=True, text=True, shell=True, check=False
# )
# print("Result: ", result.stdout)
# result.stdout holds whatever the command printed normally


# result = subprocess.run(
#     "Hello", capture_output=True, text=True, shell=True, check=False
# )
# print("Result out: ", result.stdout)
# print("Result Err: ", result.stderr)
# "Hello" is not a valid command, so stdout is empty and stderr holds
# the error message the shell produced instead

# result = subprocess.run("ping google.com", shell=True, check=False)
# print("return code: ", result.returncode)
# returncode tells us if the command succeeded or failed.
# 0 means success, any other number usually means some kind of failure.

# result = subprocess.run("ping google4cnngnjfdvdgghth.com", shell=True, check=False)
# print("return code: ", result.returncode)
# This is not a real website, so ping fails, and returncode will not be 0

# && , |
# && runs the next command only if the previous one succeeded
# | pipes the output of one command as input into the next command

# subprocess.run("echo Hello && echo World", shell= True, check=False)
# Both echo commands run one after another, since the first succeeds

# A longer chained command, split across multiple lines for readability.
# Each line ends with && so the next command only runs if the
# previous one succeeded, and the whole thing is passed as one string
cmd = (
    "echo starting process.. &&"
    "mkdir mydata &&"
    "cd mydata &&"
    "echo This is inside the folder > info.txt &&"
    "dir"
)

subprocess.run(cmd, shell=True, check=False)
# This prints a starting message, creates a folder called mydata,
# moves into it, writes text into info.txt using >, and then lists
# the folder's contents


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Use subprocess.run() to run the "dir" command (or "ls" on
#    Mac/Linux) and let it print directly to the terminal.

# 2. Use subprocess.run() with capture_output=True and text=True to
#    capture the output of the "dir" command into a variable, and
#    print it using Python's print().

# 3. Run a command that does not exist, like "bad_command_xyz", and
#    print the returncode to see that it is not 0.

# 4. Use subprocess.run() to create a new folder called practice_folder
#    using mkdir.

# 5. Chain two commands together using && to first create a folder,
#    then move into it using cd.

# 6. Use subprocess.run() to run "ping google.com" and print whether
#    it succeeded or failed, based on returncode.

# 7. Use capture_output=True to capture both stdout and stderr of a
#    command, and print both separately.

# 8. Write a command string using > to redirect the output of an
#    echo command into a text file.

# 9. Run "echo Step 1 && echo Step 2 && echo Step 3" and observe how
#    all three only run if each previous step succeeds.

# 10. Write your own multi-step command, similar to the cmd variable
#     above, that creates a folder, writes a file inside it, and then
#     lists the folder's contents.
