# Notes: Using the Boss Class (Inheritance in Action)
#
# This file shows a Boss object being used just like an Agent object,
# plus its own extra method, blow_fire(), which regular Agents do not have.

from agent import Boss

b1 = Boss("ram", 1000, 250)
# Boss inherits Agent's __init__, so it still takes name, age, health
# in the same order. Here name="ram", age=1000, health=250
print(b1.info())
# info() is inherited from Agent, Boss did not need to redefine it

b1.blow_fire()
# blow_fire() only exists on Boss, this line would fail on a plain
# Agent object, since Agent has no such method

b1.punched()
# punched() is also inherited from Agent, reduces health by 10, from 250 to 240
print(b1.info())
