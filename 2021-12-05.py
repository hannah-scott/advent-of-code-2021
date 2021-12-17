from lib import *

arr = file2arr("2021-12-05.txt")

problem(1)

parse_row = lambda row: [list(map(int, n.split(","))) for n in row.split(" -> ")]

def get_horizontal_and_vertical_lines(arr):
    out = []
    for r in arr:
        p = parse_row(r)
        if p[0][0] == p[1][0] or p[0][1] == p[1][1]:
            # Line is horizontal or vertical
            out.append(r)
    return out

def get_dimensions(arr):
    width = 0
    height = 0
    for r in arr:
        p = parse_row(r)
        for c in p:
            if c[0] > width:
                width = c[0]
            if c[1] > height:
                height = c[1]
    # Add 1 since arrays start at 0
    return width + 1, height + 1

width, height = get_dimensions(arr)

grid = []
for i in range(width):
    row = []
    for j in range(height):
        row.append(0)
    grid.append(row)

h_and_v = get_horizontal_and_vertical_lines(arr)

def min_max(x, y): 
    return min(x, y), max(x, y)

def get_points_on_line(parsed):
    difference = lambda x, y: [y[0] - x[0], y[1] - x[1]]
    diff = difference(parsed[0], parsed[1])

    if diff[0] == 0:
        min, max = min_max(parsed[0][1], parsed[1][1])
        return [[parsed[0][0], i] for i in range(min, max + 1)]
    elif diff[1] == 0:
        min, max = min_max(parsed[0][0], parsed[1][0])
        return [[i, parsed[0][1]] for i in range(min, max + 1)]
    elif diff[0] == diff[1]:
        d = -2 * (diff[0] < 0) + 1
        return [[parsed[0][0] + d * i, parsed[0][1] + d * i] for i in range(d * diff[0] + 1)]
    elif diff[0] == -1 * diff[1]:
        d = -2 * (diff[0] < 0) + 1
        return [[parsed[0][0] + d * i, parsed[0][1] - d * i] for i in range(d * diff[0] + 1)]
        

def count_crossings(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                count += 1
    return count

for line in h_and_v:
    parsed = parse_row(line)
    points = get_points_on_line(parsed)
    for p in points:
        grid[p[0]][p[1]] += 1

print(count_crossings(grid))

problem(2)

def get_valid_lines(arr):
    difference = lambda x, y: [y[0] - x[0], y[1] - x[1]]
    out = get_horizontal_and_vertical_lines(arr)
    for r in arr:
        p = parse_row(r)
        if difference(p[0], p[1])[0] == difference(p[0], p[1])[1]:
            # Line is at 45 degrees
            out.append(r)
        if difference(p[0], p[1])[0] == -1 * difference(p[0], p[1])[1]:
            # Line is at 45 degrees
            out.append(r)
    return out 

grid = []
for i in range(width):
    row = []
    for j in range(height):
        row.append(0)
    grid.append(row)

for line in get_valid_lines(arr):
    parsed = parse_row(line)
    points = get_points_on_line(parsed)
    for p in points:
        grid[p[0]][p[1]] += 1

print(count_crossings(grid))

def print_grid(grid):
    for row in grid:
        string = ""
        for c in row:
            if c == 0:
                string += ". "
            else:
                string += "{} ".format(c)
        print(string)


