'''A university has three departments: Mathematics, Physics, and Chemistry. Each department requires a certain
number of classrooms and faculty members. The Mathematics department requires 3 classrooms and 5 faculty
members, the Physics department requires 2 classrooms and 4 faculty members, and the Chemistry department
requires 4 classrooms and 6 faculty members. The university has 15 classrooms and 25 faculty members available.
Determine the optimal allocation of classrooms and faculty members to maximize the overall departmental
capacity.'''

from scipy.optimize import linprog

