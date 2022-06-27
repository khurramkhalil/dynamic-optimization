from gekko import GEKKO
import numpy as np

# Initialize the model
m = GEKKO(remote=False)

# define variables
x1, x2, x3, x4 = [m.Var() for i in range(4)]

# Initial values
x1.value = 1
x2.value = 5
x3.value = 5
x4.value = 1

# lower bound
x1.lb = 1
x2.lb = 1
x3.lb = 1
x4.lb = 1

# upper bound
x1.ub = 5
x2.ub = 5
x3.ub = 5
x4.ub = 5

# define parameter
param = m.Param(value=40)

#