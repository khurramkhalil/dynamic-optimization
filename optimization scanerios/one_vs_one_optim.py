import numpy as np
from ortools.linear_solver import pywraplp

# Cost matrix
costs = np.array([
    [20, 10],
    [10, 5]
])

num_workers = len(costs)
num_tasks = len(costs[0])

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

# x[i, j] is an array of 0-1 variables, which will be 1
# if worker i is assigned to task j.
x = {}
for i in range(num_workers):
    for j in range(num_tasks):
        x[i, j] = solver.IntVar(0, 1, '')

# Each worker is assigned to at most 1 task.
for i in range(num_workers):
    solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

# Each task is assigned to exactly one worker.
for j in range(num_tasks):
    solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

objective_terms = []
for i in range(num_workers):
    for j in range(num_tasks):
        objective_terms.append(costs[i][j] * x[i, j])

solver.Minimize(solver.Sum(objective_terms))

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print(f'Total cost = {solver.Objective().Value()}\n')
    for i in range(num_workers):
        for j in range(num_tasks):
            # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
            if x[i, j].solution_value() > 0.5:
                print(f'Worker {i} assigned to task {j}.' + f' Cost: {costs[i][j]}')
else:
    print('No solution found.')
