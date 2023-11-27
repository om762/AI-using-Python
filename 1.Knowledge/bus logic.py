from logic import *

bus = Symbol('Bus') # Bus busStop pe ayegi
college = Symbol('College') # Will go to college
canteen = Symbol('Canteen') # Will go to canteen
chai = Symbol('Chai')
poha = Symbol('Poha')

know = And(
            Implication(Or(chai, poha),canteen),
            Implication(Or(college, canteen), bus),
            Implication(canteen, college),
            Not(bus),
            Implication(canteen, college),
            Implication(Not(bus), Not(college))
)

print(model_check(know, poha))