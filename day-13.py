from lib import *

arr = file2arr("day-13.txt")

def get_instructions(arr):
    coords = []
    folds = []

    for row in [n for n in arr if n != '']:
        cs = row.split(",")
        if len(cs) > 1:
            coords.append([int(n) for n in cs])
        else:
            f = cs[0][cs[0].index("g ") + 2:].split("=")
            if f[0] == 'x':
                folds.append([int(f[1]), 0])
            else:
                folds.append([0, int(f[1])])
    return coords, folds

def initialize_grid(arr):
    coords, folds = get_instructions(arr)
    
    get_dimensions = lambda arr: [max([n[0] for n in arr]) + 1, max([n[1] for n in arr]) + 1]

    dims = get_dimensions(coords)

    grid = [[0 for _ in range(dims[0])] for _ in range(dims[1])]

    for c in coords:
        grid[c[1]][c[0]] = 1

    return coords, folds, grid

coords, folds, grid = initialize_grid(arr)

def fold_grid(grid, fold):
    if fold[0] > 0:
        # left fold
        new_grid = [[0 for _ in range(fold[0])] for _ in range(len(grid))]
        for j in range(len(grid)):
            for i in range(fold[0]):
                if grid[j][i] > 0 or grid[j][len(grid[0]) - i - 1] > 0:
                    new_grid[j][i] = 1
    else:
        # up fold
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(fold[1])]
        for j in range(fold[1]):
            for i in range(len(grid[0])):
                if grid[j][i] > 0 or grid[len(grid) - j - 1][i] > 0:
                    new_grid[j][i] = 1
    return new_grid

def count_ones(grid):
    count = 0
    for row in grid:
        for c in row:
            count += c
    return count

problem(1)

print(count_ones(fold_grid(grid, folds[0])))

problem(2)

for f in folds:
    grid = fold_grid(grid, f)

print_grid(grid, charset=[" ", "#"])