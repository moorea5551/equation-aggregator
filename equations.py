from consolemenu import *
from consolemenu.items import *
import math

def pythagoreanTheorem():
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    Screen().println(a + "^2 + " + b + "^2 = " + c + "^2")

    answer = 0
    if a == "?":
        Screen().println("sqrt(c^2 - b^2)")
        answer = math.sqrt(int(c) ** 2 - int(b) ** 2)
    elif b == "?":
        Screen().println("sqrt(c^2 - a^2)")
        answer = math.sqrt(int(c) ** 2 - int(a) ** 2)
    elif c == "?":
        Screen().println("sqrt(a^2 + b^2)")
        answer = math.sqrt(int(a) ** 2 + int(b) ** 2)

    Screen().println(answer)
    Screen().input('Press [Enter] to continue')