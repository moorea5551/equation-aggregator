from consolemenu import *
from consolemenu.items import *
from equations import *

menu = ConsoleMenu("Equation Aggregator", "So you don't have to remember anything")

pythagoreanTheoremFunctionItem = FunctionItem("Pythagorean Theorem", pythagoreanTheorem)
menu.append_item(pythagoreanTheoremFunctionItem)

menu.show()