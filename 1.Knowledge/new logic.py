from logic import *

# Define symbolic variables
A = Symbol('A')
B = Symbol('B')
C = Symbol('C')
D = Symbol('D')
E = Symbol('E')

knowledge = And(
    # Complex implications
    Implication(And(A, B), C),
    Implication(D, Not(C)),

    # XOR relationship
    Or(And(A, B), And(Not(A), Not(B)), And(C, D)),

    # Nested implications
    Implication(And(A, B), Implication(And(C, D), E)),

    # Complex combination of conditions
    Or(And(A, B), And(C, D), And(E, Not(A))),
    
    # Recursive relationship
    Implication(Or(A, B), E)
)

query = And(
    # Complex combination of conditions
    Or(And(A, B), And(C, D), And(E, Not(A))),
    
    # Nested implications
    Implication(And(A, B), Implication(And(C, D), E)),

    # XOR relationship
    Or(And(A, B), And(Not(A), Not(B)), And(C, D)),

    # Recursive relationship
    Implication(Or(A, B), E)
)
print(model_check(knowledge, query))