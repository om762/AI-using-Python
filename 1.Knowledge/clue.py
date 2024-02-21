import termcolor

from logic import *

vishal = Symbol("Vishal Yadav")
om = Symbol("Omprakash")
kavita = Symbol("Kavita")
characters = [vishal, om, kavita]

canteen = Symbol("canteen")
classRoom = Symbol("classRoom")
library = Symbol("library")
rooms = [canteen, classRoom, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
pencil = Symbol("pencil")
weapons = [knife, revolver, pencil]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(vishal, om, kavita),
    Or(canteen, classRoom, library),
    Or(knife, revolver, pencil)
)

# Initial cards
knowledge.add(And(
    Not(vishal), Not(classRoom), Not(revolver)
))

# Unknown card
knowledge.add(Or(
    Not(kavita), Not(library), Not(pencil)
))

# Known cards
knowledge.add(Not(om))
knowledge.add(Not(canteen))

check_knowledge(knowledge)
