# Notes: OOP - Classes and Objects
#
# OOP - classes and objects
# grp data + functions together
# Object Oriented Programming (OOP) is a way of organizing code by
# grouping related data (variables) and behavior (functions) together
# into a single unit, instead of keeping them scattered separately.

# class - template
# object - instance of a class
#  class  -> recipe
#  instructions -> methods (fun inside class)
#  list of ingredients ->
#  dish -> object
# A class is like a recipe, it defines what something should look
# like and what it can do, but it is not the actual thing yet.
# An object is an actual dish made using that recipe, a real, usable
# item created from the class. We can make many objects from one class.


#  game - players - 100
#  name, health, strength, weapon

#  player1_name, p1_health
# Without OOP, storing data for 100 players would mean 100 separate
# sets of variables, like player1_name, player1_health, player2_name,
# player2_health, and so on. A class solves this by letting each
# player be one object, holding all its own data together.

#  Player

# class Person:
#     name = "Sam"
#     age =20
# This class has two class attributes, name and age, with default values

# p1 = Person()
# print("obj p1: ", p1)
# print("obj p1 name: ", p1.name)
# print("obj p1 age: ", p1.age)
# p1 is an object (instance) created from the Person class, and it
# has access to the class's attributes using dot notation

# p1.name = "Asha"
# p1.age = 25
# print("after p1 name: ", p1.name)
# print("after p1 age: ", p1.age)
# Assigning a new value like this creates the attribute directly on
# p1 itself, separate from the class's own name and age

# p2 = Person()

# print("obj p2 name: ", p2.name)
# print("obj p2 age: ", p2.age)
# p2 is a completely different object from p1. Since we never changed
# p2's own name/age, it still shows the original class values, "Sam"
# and 20, unaffected by whatever we did to p1

# class Car:
#     color = "White"
# A simple class with just one attribute, to show that classes can
# represent anything, not just people

# A class can also have methods, functions defined inside the class,
# which describe what an object of this class can do

# class Mathematics:
#     # def greet():
#     def greet(self):
#         print("Hello world")
# self refers to the object calling the method. It must be the first
# parameter of every method, Python passes it automatically, we do
# not pass it ourselves when calling the method

# math = Mathematics()
# # Mathematics.greet(math)
# math.greet()
# math.greet() is really just a shortcut for Mathematics.greet(math),
# Python automatically passes math in as self

# class Mathematics:
#     # def greet():
#     def greet(self):
#         print("Hello world")
#         return "Hi"

# math = Mathematics()
# # Mathematics.greet(math)
# math.greet()
# print(math.greet())
# Just like a normal function, a method can also return a value using
# return, which we can then print or store

# Factorial(n), list product, dot product of two lists
# fact(5) - 1*2*3*4*5 -> 120
# [1, 2,3 , 4, 5, 6] -> 720
# [1, 2,3], [4, 5, 6] -> 4, 10, 18 -> 32
# A class can group multiple related methods together, here all
# related to different kinds of mathematical calculations


# class Mathematics:
#     def factorial(self, n):
#         result = 1
#         for i in range(1, n + 1):
#             result = result * i
#         return result

#     def list_product(self, lst):
#         prod = 1
#         for x in lst:
#             prod = prod * x
#             # prod *= x
#         return prod

#     def dot_product(self, lst1, lst2):
#         if len(lst1) != len(lst2):
#             raise ValueError("lists must be same length")
#         return sum(a * b for a, b in zip(lst1, lst2))
# dot_product multiplies matching pairs from both lists (using zip)
# and adds up all the results, raising an error first if the lists
# are not the same length


# math = Mathematics()
# print(math.factorial(5))
# print(math.list_product([1, 2, 3, 4]))
# print(math.dot_product([1, 2, 3], [4, 5, 6]))

# __init__
# __init__ is a special method that runs automatically every time a
# new object is created from the class. It is commonly used to set
# up the object's starting data, this is called a constructor.


# class Person:
#     def __init__(self):
#         print("Obj created!!")

#     def run(self):
#         print("Person is running")


# p1 = Person()
# p2 = Person()
# p3 = Person()
# p4 = Person()
# "Obj created!!" prints four times here, once automatically for
# each object as it is created

# class Person:
#     def __init__(name, age):
#         print("Obj created!!")

#     def run(self):
#         print("Person is running")

# p1 = Person("Sam", 25)
# This __init__ is missing self as its first parameter, so this
# actually fails, Python tries to pass the object itself as the first
# argument (into name), then "Sam" and 25 have nowhere to go

# The correct way, self must always come first, followed by any other
# parameters we want to pass in when creating the object
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print(f"{self.name} is running")

# p1 = Person("Sam", 25)
# p1.run()
# print(p1.name, p1.age)
# self.name = name and self.age = age store the given values onto
# this specific object, so each object can hold its own separate data,
# even though they are all created from the same class
