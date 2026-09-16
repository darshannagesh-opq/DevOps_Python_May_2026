# Notes: Using the Agent Class
#
# This file imports and uses the Agent class defined in agent.py,
# showing how a class written in one file can be reused in another,
# the same way modules were reused earlier.

from agent import Agent

p1 = Agent("Sam", 25)
# Creates a new Agent object. Since no health value is given, __init__
# uses its default of 100, and prints "Welcome to the game"
print(p1.info())

p1.punched()
# Reduces p1's health by 10, from 100 to 90
p1.current_health()

p1.shot()
# Reduces p1's health by 25, from 90 to 65
p1.current_health()

print(p1.is_alive())
# health is 65, which is greater than 0, so this prints True

p1.shot()
p1.shot()
p1.shot()
# Three more shots, each -25, taking health from 65 down to 0
# (clamped at 0, never going negative, because of the check in shot())
p1.current_health()
print(p1.is_alive())
# health is now 0, which is not greater than 0, so this prints False
