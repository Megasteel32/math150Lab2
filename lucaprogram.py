from sympy import *

x = symbols('x')

solution1 = solve(3*x + 10 < 43, x)
print(solution1)

solution2 = solve(-1 < (7-x)/3, x) and solve((7-x)/3 <= 4, x)
print(solution2)

solution3 = solve(abs(2*x + 3) > 9, x)
print(solution3)