# Notes: while Loop in Python
#
# A while loop keeps running the code inside it as long as a condition
# stays True. Unlike a for loop, we do not know in advance how many
# times it will run, it depends on when the condition becomes False.

#  as long as cond is T

# while cond:
    # code
# Before every round, Python checks the condition. If it is True,
# the code runs, then it checks again. If it is False, the loop stops.

# i = 0
# while i<=5:
#     print(i)
#     i += 1
    # i = i+1
# i starts at 0. After printing, i is increased by 1 each time.
# Without this increase, the condition would always stay True and
# the loop would never stop, this is called an infinite loop.

# # keep adding consecutive ints 1, 2, 3.. until the running sum becomes greater than or equal to N
# N = int(input("Enter a number: "))
# # 1, 2, 3, 4, 5, 6, ....

# i = 1
# s = 0

# while s < N:
#     s = s + i
#     # s += i
#     print(f"After adding {i} -> sum {s} ")
#     i += 1
# Here we do not know how many rounds it will take in advance,
# it depends on the value of N, which is why while is used instead of for.


# A practical example: a login system with a limited number of attempts
# break stops the loop right away, once the correct details are entered
# else on a while loop runs only if the loop ends normally, without a break,
# which here means the user ran out of attempts

correct_user = "admin"
correct_pass = "admin123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user = input("username: ")
    password = input("password: ")

    if user == correct_user and password == correct_pass:
        print("Login !!!")
        break
    else:
        attempts += 1
        print("incorrect")
        print("left: ", max_attempts-attempts)
else:
    print("locked")
# The loop keeps asking for username and password while attempts is
# below max_attempts. A correct login breaks out early. If attempts
# reaches max_attempts without a correct login, the while loop ends
# normally and the else block prints "locked"


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Print numbers from 1 to 10 using a while loop.

# 2. Take a number as input and print its multiplication table
#    from 1 to 10, using a while loop instead of a for loop.

# 3. Find the sum of all numbers from 1 to 50 using a while loop.

# 4. Take a number as input and keep dividing it by 2 until it
#    becomes less than 1, printing the value at each step.

# 5. Print all even numbers between 1 and 20 using a while loop.

# 6. Take a number as input and count how many digits it has,
#    using a while loop (hint, keep dividing by 10).

# 7. Write a while loop that keeps asking the user to enter a number
#    until they enter 0, then stop.

# 8. Take a number as input and check if it is a prime number,
#    using a while loop.

# 9. Simulate a simple countdown from 10 to 1 using a while loop,
#    and print "Liftoff!" at the end.

# 10. Write a guessing game, a fixed number is stored in a variable,
#     and the user keeps entering guesses in a while loop until they
#     guess it correctly. Print "Too high" or "Too low" for wrong guesses.
