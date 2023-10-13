from logic import *
import termcolor as tc

class_Mate = ['Vidit', 'Suresh', 'Madhuri']
places = ['Delhi', 'Varanasi', 'Jabalpur']

symbols = []

knowledge = And()

for person in class_Mate:
    for college in places:
        symbols.append(Symbol(f'{person} in {college}'))

# Each belongs to a college
for person in class_Mate:
    knowledge.add(Or(
        Symbol(person + ' in Jabalpur'),
        Symbol(person + ' in Delhi'),
        Symbol(person + ' in Varanasi')
    ))

# One college is for only one
for std in class_Mate:
    for p1 in places:
        for p2 in places:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(person + ' in ' + p1), Not(Symbol(person +  ' in ' + p2)))
                )

# No one can live in two college
for college in places:
    for std1 in class_Mate:
        for std2 in class_Mate:
            if std1 != std2:
                knowledge.add(
                    Implication(Symbol(std1 + ' in ' + college), Not(Symbol(std2 + ' in ' + college)))
                )

# What I know
# 1.
knowledge.add(
    Or(Symbol('Vidit in Delhi'), Symbol('Vidit in Varanasi'))
)

# 2.
knowledge.add(
    Not(Symbol('Madhuri in Delhi'))
)

# 3.
knowledge.add(Symbol('Suresh in Varanasi'))

for s in symbols:
    val = model_check(knowledge, s)
    print(s, end= '') #
    if val:
        tc.cprint(" True", "green")
    else:
        tc.cprint(" False", "red")
