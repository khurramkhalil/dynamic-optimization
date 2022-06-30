import numpy as np
from gekko import GEKKO

# Initialize model
m = GEKKO(remote=False)

# Initialize time stamps
nt = 101
m.time = np.linspace(0, 1, nt)

# Initialize model variables
x1 = m.Var(value=1)
x2 = m.Var(value=0)
u = m.Var(value=0.75)

# Get final time stamp
p = np.zeros(nt)
p[-1] = 1
final = m.Param(value=p)

# Initialize equations
m.Equation(x1.dt() == u)
m.Equation(x2.dt() == x1 ** 2 + u ** 2)

# Objective function
m.Obj(x2 * final)

# Set global options
m.options.IMODE = 6  # dynamic optimization

# Solve the simulations
m.solve()

# Results
print(f'Optimized x2 value: {x2.value[-1]}')

if __name__ == "__main__":
    pass
