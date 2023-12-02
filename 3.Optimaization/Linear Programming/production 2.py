'''A company produces two products, A and B. The production of each unit of A requires 2 hours of labor and 1
hour of machine time, while each unit of B requires 1 hour of labor and 3 hours of machine time. The company
has 100 hours of labor and 90 hours of machine time available each day. Product A sells for $5 per unit, and
product B sells for $8 per unit. Determine the number of units of each product the company should produce to
maximize revenue.'''

from scipy.optimize import linprog

cost_fuction = [-5, -8]  # For Revenue = 5x + 8x
labor_cofficient = [2, 1]  # Labor hours constraint: 2x + 1y <= 100
machine_time = [1, 3]   # Machine hours constraint: 1x + 3y <= 90
constraint = [100, 90]


result = linprog(
    cost_fuction,
    A_ub = [labor_cofficient, machine_time],
    b_ub = constraint
)

if result.success:
    print(f"A: {round(result.x[0], 2)} units")
    print(f"B: {round(result.x[1], 2)} units")
else:
    print("No solution")