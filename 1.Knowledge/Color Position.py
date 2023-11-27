from logic import *

colors = ["red", "blue", "green", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color} at {i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color} at 0"),
        Symbol(f"{color} at 1"),
        Symbol(f"{color} at 2"),
        Symbol(f"{color} at 3")
    ))

# Only one position per color.
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color} at {i}"), Not(Symbol(f"{color} at {j}"))
                ))

# Only one color per position.
for i in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(Implication(
                    Symbol(f"{c1} at {i}"), Not(Symbol(f"{c2} at {i}"))
                ))

knowledge.add(Or(
    And(Symbol("red at 0"), Symbol("blue at 1"), Not(Symbol("green at 2")), Not(Symbol("yellow at 3"))),
    And(Symbol("red at 0"), Symbol("green at 2"), Not(Symbol("blue at 1")), Not(Symbol("yellow at 3"))),
    And(Symbol("red at 0"), Symbol("yellow at 3"), Not(Symbol("blue at 1")), Not(Symbol("green at 2"))),
    And(Symbol("blue at 1"), Symbol("green at 2"), Not(Symbol("red at 0")), Not(Symbol("yellow at 3"))),
    And(Symbol("blue at 1"), Symbol("yellow at 3"), Not(Symbol("red at 0")), Not(Symbol("green at 2"))),
    And(Symbol("green at 2"), Symbol("yellow at 3"), Not(Symbol("red at 0")), Not(Symbol("blue at 1")))
))

knowledge.add(And(
    Not(Symbol("blue at 0")),
    Not(Symbol("red at 1")),
    Not(Symbol("green at 2")),
    Not(Symbol("yellow at 3"))
))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
