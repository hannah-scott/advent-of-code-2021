from lib import *

get = lambda arr, x: arr[x[1]][x[0]]

arr = file2arr("2021-12-09.txt", lambda x: [int(n) for n in x])

problem(1)

def get_neighbours(arr, coords):
    x = coords[0]
    y = coords[1]

    neighbour_coords = [
        [x + 1, y],
        [x, y + 1],
        [x - 1, y],
        [x, y - 1]
    ]

    neighbours = []
    ncs = []

    for nc in neighbour_coords:
        if nc[1] in range(len(arr)) and nc[0] in range(len(arr[nc[1]])):
            neighbours.append(arr[nc[1]][nc[0]])
            ncs.append(nc)
    return neighbours, ncs

def is_low_point(arr, coords):
    neighbours, _ = get_neighbours(arr, coords)
    for n in neighbours:
        if n <= arr[coords[1]][coords[0]]:
            return False
    return True

def get_risk_level(arr, coords):
    if is_low_point(arr, coords):
        return arr[coords[1]][coords[0]] + 1
    else:
        return 0

def get_total_risk(arr):
    risk = 0
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            risk += get_risk_level(arr, [i,j])
    return risk

print(get_total_risk(arr))

problem(2)

def get_basin_map(arr):
    basin = []
    for j in range(len(arr)):
        row = []
        for i in range(len(arr[j])):
            if arr[j][i] == 9:
                row.append(0)
            else:
                row.append(1)
        basin.append(row)
    return basin

# Start at a location
# Get a list of all adjacent points that aren't:
# - visited
# - or 0
# Add those to a list

def get_basins(arr):
    basins = []
    visited = []
    
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if [i, j] not in visited:
                if get(arr, [i, j]) == 1:
                    basin, vs = get_basin(arr, [i, j])
                    basins.append(basin)
                    for v in vs:
                        if v not in visited:
                            visited.append(v)

    return basins

def get_basin(arr, coords):
    
    current = coords
    visited = [current]
    basin = [current]

    _, ncs = get_neighbours(arr, current)
    to_visit = ncs

    while len(to_visit) > 0:
        current = to_visit[-1]
        to_visit = to_visit[:-1]
        if get(arr, current) == 1 and current not in visited:
            visited.append(current)
            basin.append(current)
            _, ncs = get_neighbours(arr, current)
            for nc in ncs:
                if nc not in visited and nc not in to_visit:
                    to_visit.append(nc)
    return basin, visited

def get_basin_sizes(arr):
    basins = get_basins(arr)
    return list(map(len, basins))

basin_sizes = get_basin_sizes(get_basin_map(arr))

basin_sizes.sort()

product = 1
for size in basin_sizes[-3:]:
    product *= size
print(product)