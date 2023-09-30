from logic import *
import termcolor

# Who came to home
harsh = Symbol("Harsh")  # Harsh ghar aya tha
ghanshyam = Symbol("Ghanshyam") # Ghanshyam ghar aya tha
akshay = Symbol("Akshay") # Akshay ghar aya tha
friends = [harsh, ghanshyam, akshay]

# How he traveled
bike = Symbol("Bike") # Car se koi aya
walk = Symbol("Walk") # Car se koi aya
car = Symbol("Car") # Car se koi aya
mediums = [bike, walk, car]

# Kaha se aya
khandwa = Symbol("Khandwa")
indore = Symbol("Indore")
delhi = Symbol("Delhi")
locations = [khandwa, indore, delhi]

Noun = locations + mediums+ friends

def check_knowledge(knowledge):
    for symbol in Noun:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

# Initial State
knowledge = And(
    Or(harsh, ghanshyam, akshay),
    Or(car, walk, bike),
    Or(indore, khandwa, delhi)
)

# Impossible Condition
knowledge.add(
    And(Not(akshay), Not(car), Not(delhi))
)

# Ghanshyam ye nhi karega
knowledge.add(
    Or(Not(ghanshyam), Not(walk), Not(indore))
)

#Somthing that confirm

# Known cards
knowledge.add(Not(harsh))
knowledge.add(Not(khandwa))

check_knowledge(knowledge)