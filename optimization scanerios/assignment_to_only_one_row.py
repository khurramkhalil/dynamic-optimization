import numpy as np
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

import time

t1 = time.time()
costs = [
    [20, 40, 160, 100, 700, 100, 100, 1100],
    [100, 180, 10, 30, 100, 100, 1200, 180, 200],
    [100, 90, 100, 100, 50, 5, 100, 900],
    [1000, 100, 100, 100, 100, 100, 60, 70]
]






def main():
    costs = [
        [20, 40, 100, 100, 100, 100, 100, 100],
        [100, 100, 10, 30, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 50, 5, 100, 100],
        [100, 100, 100, 100, 100, 100, 60, 70]
    ]

    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Create the mip solver with the SCIP backend.
    # solver = cp_model.CpModel()

    # Model
    model = cp_model.CpModel()

    # Variables
    x = []
    for i in range(num_workers):
        t = []
        for j in range(num_tasks):
            t.append(model.NewBoolVar(f'x[{i},{j}]'))
        x.append(t)

    # Constraints
    # Each worker is assigned to at most one task.
    for i in range(num_workers):
        model.AddAtMostOne(x[i][j] for j in range(num_tasks))

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        model.AddExactlyOne(x[i][j] for i in range(num_workers))

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i][j])
    model.Minimize(sum(objective_terms))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total cost = {solver.ObjectiveValue()}')
        print()
        for i in range(num_workers):
            for j in range(num_tasks):
                if solver.BooleanValue(x[i][j]):
                    print(
                        f'Worker {i} assigned to task {j} Cost = {costs[i][j]}')
    else:
        print('No solution found.')


if __name__ == '__main__':
    main()

# num_workers = len(costs)
# num_tasks = len(costs[0])
#
# # Create the mip solver with the SCIP backend.
# solver = cp_model.CpModel()
#
#
#
# # x[i, j] is an array of 0-1 variables, which will be 1
# # if worker i is assigned to task j.
# x = {}
# for i in range(num_workers):
#     for j in range(num_tasks):
#         x[i, j] = solver.IntVar(0, 1, '')
#
# print(x)
# # Each worker is assigned to at most 1 task.
# for i in range(num_workers):
#     solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)
#
# # Each worker is assigned to only his row
# for k in range(num_workers):
#     # solver.Add((x[k, l] for l in range(num_tasks)) == 1)
#     # solver.Add(solver.Sum([x[k, j] for j in range(num_tasks)]) <= 1)
#     for l in range(num_tasks):
#         solver.Add(x[k, l] == 1)
#
#     solver.Add(solver.Sum([x[k, j] for j in range(num_tasks)]) <= 1)
#
# # Each task is assigned to exactly one worker.
# for j in range(num_tasks):
#     solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)
#
# objective_terms = []
# for i in range(num_workers):
#     for j in range(num_tasks):
#         objective_terms.append(costs[i][j] * x[i, j])
#
# solver.Minimize(solver.Sum(objective_terms))
#
# status = solver.Solve()
#
# if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
#     print(f'Total cost = {solver.Objective().Value()}\n')
#     for i in range(num_workers):
#         for j in range(num_tasks):
#             # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
#             if x[i, j].solution_value() > 0.5:
#                 print(f'Worker {i} assigned to task {j}.' + f' Cost: {costs[i][j]}')
# else:
#     print('No solution found.')
#
# print(f'Total time taken: {time.time() - t1}')
#