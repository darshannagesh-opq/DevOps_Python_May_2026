# Notes: A Practical Class Example (Agent) and Inheritance (Boss)
#
# This file builds a real class, Agent, for a simple game, bringing
# together everything from oops.py: __init__, self, attributes and methods.

#  age, name, health
#  punched = -10
#  shot = -25
# current_health
# info
# This is the plan before writing the class: what data each agent
# needs (age, name, health), and what actions can affect health
# (getting punched, getting shot), plus some helper methods.


class Agent:
    def __init__(self, name, age, health=None):
        print("Welcome to the game")
        self.name = name
        self.age = age
        # health=None as a default lets the caller skip giving a
        # health value. If they don't provide one, health becomes 100,
        # otherwise it uses whatever value they gave.
        self.health = 100 if health is None else health
        self.alive = True

    def current_health(self):
        print(f"{self.name} current health: {self.health}")

    def punched(self):
        self.health -= 10
        # health should never go below 0, so we clamp it here
        if self.health < 0:
            self.health = 0

    def shot(self):
        self.health -= 25
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        # This both updates self.alive based on the current health,
        # and returns that same value, so calling it keeps the
        # object's state up to date and also gives us an answer
        self.alive = self.health > 0
        return self.alive

    def info(self):
        return f"{self.name}: age= {self.age}, health={self.health}, alive={self.alive}"


# Inheritance
# Inheritance lets one class (Boss) reuse everything from another
# class (Agent), without rewriting it. Boss gets all of Agent's
# attributes and methods automatically, and can also add its own.
class Boss(Agent):
    def blow_fire(self):
        print(f"{self.name} uses Blow fire")
# Boss(Agent) means Boss inherits from Agent. A Boss object still has
# name, age, health, alive, and can still call punched(), shot(),
# current_health(), is_alive() and info(), all inherited from Agent.
# blow_fire() is a new method that only Boss has, Agent objects
# cannot use it.
