from gekko import GEKKO
import numpy as np

# Initialize the model
m = GEKKO(remote=False)

# Define variables
x1, x2, x3, x4 = [m.Var() for i in range(4)]

# Initial values
x1.value = 1
x2.value = 5
x3.value = 5
x4.value = 1

# lower bound
x1.LOWER = 1
x2.LOWER = 1
x3.LOWER = 1
x4.LOWER = 1

# upper bound
x1.UPPER = 5
x2.UPPER = 5
x3.UPPER = 5
x4.UPPER = 5

# Define parameter
param = m.Param(value=40)

# Define equations
m.Equation(x1 * x2 * x3 * x4 >= 25)
m.Equation(x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 4 == param)

# Objective
m.Obj(x1 * x4 * (x1 + x2 + x3) + x3)

# Set global options
m.options.IMODE = 3  # steady state optimization

# Solve simulation
m.solve()

# Results
print(f'x1, x2, x3, x4: {x1.value, x2.value, x3.value, x4.value}')

if __name__ == "__main__":
    pass
