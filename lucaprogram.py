from sympy import *
from matplotlib import pyplot
import numpy as np

x = symbols('x')
# Part 1
solution1 = solve(3*x + 10 < 43, x)
print(solution1)

solution2 = solve(-1 < (7-x)/3, x) and solve((7-x)/3 <= 4, x)
print(solution2)

solution3 = solve(abs(2*x + 3) > 9, x)
print(solution3)

# Part 2
x1, y1 = input("What is the first point? ").split(", ")
x2, y2 = input("What is the second point? ").split(", ")
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)
slope = (y2-y1)/(x2-x1)
intercept = y1 - slope*x1
print("The equation of the line is y =",slope,"x +",intercept)

# Part 3
graph_var = np.safe_eval(x**2)
domain = np.array(range(-10, 10))
print(domain)
print(graph_var)