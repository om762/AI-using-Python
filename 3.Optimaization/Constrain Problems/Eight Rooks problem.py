'''
The 8-Rooks problem is a classic chessboard puzzle that involves placing eight Rooks on an 8x8 chessboard in
such a way that no two Rooks threaten each other. Rooks can move horizontally or vertically but not diagonally.
The challenge is to find a configuration where no two Rooks share the same row or column. 
'''

from constraint import *

problem = Problem()
size = 4  # Size of board

rows = range(size)
cols = range(size)

# Adding Variables
problem.addVariables(rows, cols)  # Rows are variables and cols are Domain for rows

# Add Constraint
# No two rook can be in the same row or column.
for col1 in cols:
    for col2 in cols:
        if col1 < col2:
            problem.addConstraint(lambda x, y : x != y, (col1, col2))
     
# Get solutions
solutions = problem.getSolution()

print(solutions)
