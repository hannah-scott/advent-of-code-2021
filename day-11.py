from lib import *

problem(1)

arr = file2arr("day-11.txt", lambda x: [int(n) for n in x])

def get_neighbours(arr, coords):
    x = coords[0]
    y = coords[1]

    neighbour_coords = [
        [x + 1, y],
        [x, y + 1],
        [x - 1, y],
        [x, y - 1],
        [x - 1, y - 1],
        [x + 1, y - 1],
        [x - 1, y + 1],
        [x + 1, y + 1]
    ]

    neighbours = []
    ncs = []

    for nc in neighbour_coords:
        if nc[1] in range(len(arr)) and nc[0] in range(len(arr[nc[1]])):
            neighbours.append(arr[nc[1]][nc[0]])
            ncs.append(nc)
    return neighbours, ncs

def get_flash_locations(arr):
    flash_locations = []
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] > 9:
                flash_locations.append([i, j])
    return flash_locations

def run_step(arr):
    flashed = []
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            arr[j][i] += 1
    
    fs = get_flash_locations(arr)
    while len(fs) > 0:
        l = fs[-1]
        fs = fs[:-1]
        if l not in flashed:
            flashed.append(l)
        _, ncs = get_neighbours(arr, l)
        for nc in ncs:
            arr[nc[1]][nc[0]] += 1

        new = get_flash_locations(arr)
        for n in new:
            if n not in fs and n not in flashed:
                fs.append(n)
        
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] > 9:
                arr[j][i] = 0
    return arr, len(flashed)

def run_steps(arr, n):
    sum = 0
    for _ in range(n):
        arr, count = run_step(arr)
        sum += count
    return sum

print(run_steps(arr, 100))

problem(2)

# Reset arr, since we're updating it
arr = file2arr("day-11.txt", lambda x: [int(n) for n in x])

def is_all_zeros(arr):
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] > 0:
                return False
    return True

def find_sync(arr):
    sync = False
    count = 0
    while not sync:
        arr, _ = run_step(arr)
        count += 1
        sync = is_all_zeros(arr)
    return count

print(find_sync(arr))