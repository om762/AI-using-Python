from logic import *

deepak = Symbol('Deepak')    # Deepak is a suspect
rohit = Symbol('Rohit')      # Rohit is a suspect
sanya = Symbol('Sanya')      # Sanya is a suspect

# Define symbolic variables for statements
statement_deepak = Symbol('StatementDeepak')   # Deepak's statement
statement_rohit = Symbol('StatementRohit')     # Rohit's statement
statement_sanya = Symbol('StatementSanya')     # Sanya's statement

# Define symbolic variables for car colors
red_car = Symbol('RedCar')      # The stolen car is red
blue_car = Symbol('BlueCar')    # The stolen car is blue
green_car = Symbol('GreenCar')  # The stolen car is green

# Define the logical rules
know = And(
    # The stolen car is one of the available colors.
    Or(red_car, blue_car, green_car),

    # If Deepak is telling the truth, then the car is red.
    Implication(statement_deepak, red_car),

    # If Rohit is telling the truth, then the car is not green.
    Implication(statement_rohit, Not(green_car)),

    # If Sanya is telling the truth, then the car is blue or green.
    Implication(statement_sanya, Or(blue_car, green_car)),

    # At least one of them is telling the truth.
    Or(statement_deepak, statement_rohit, statement_sanya),

    # They cannot all be telling the truth.
    Not(And(statement_deepak, statement_rohit, statement_sanya)),

    # Deepak and Rohit cannot both be telling the truth.
    Not(And(statement_deepak, statement_rohit)),

    # Sanya is not telling the truth about the car being green.
    Not(And(statement_sanya, green_car))
)

# Check who is telling the truth and determine the color of the stolen car
solution = None
for color in [red_car, blue_car, green_car]:
    if model_check(know, And(color, Or(statement_deepak, statement_rohit, statement_sanya))):
        solution = color
        break

if solution:
    print(f"The stolen car is {solution}.")
    if solution == red_car:
        print("Deepak is telling the truth.")
    elif solution == blue_car:
        print("Sanya is telling the truth.")
    else:
        print("Rohit is telling the truth.")
else:
    print("There is no conclusive solution to the puzzle.")
