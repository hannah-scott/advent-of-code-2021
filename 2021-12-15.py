from lib import *
import time

arr = file2arr("2021-12-15.txt", lambda x: [int(n) for n in x])

get_dimensions = lambda x: [len(x[0]), len(x)]

def get_neighbours(arr, coords):
    x = coords[0]
    y = coords[1]

    neighbour_coords = [
        [x + 1, y],
        [x, y + 1],
        [x - 1, y],
        [x, y - 1]
    ]

    return [nc for nc in neighbour_coords if nc[1] in range(len(arr)) and nc[0] in range(len(arr[nc[1]]))]

def a_star_search(arr):
    BIG = 10000000000
    start = [0, 0]
    end = [len(arr[0]) - 1, len(arr) - 1]
    
    h = lambda x: ((abs(x[0][0] - end[0]) + abs(x[0][1] - end[1])))

    def g(n):
        return n[2]

    f = lambda x: g(x) + h(x)
    
    to_visit = []

    for j in range(len(arr)):
        for i in range(len(arr[j])):
            to_visit.append([[i, j], None, BIG])

    to_check = [[start, None, 0, BIG]]

    while len(to_check) != 0:
        # current = smallest(to_check)
        current = to_check[0]
        to_check = to_check[1:]

        if current[0] == end:
            return current

        for nc in get_neighbours(arr, current[0]):
            neighbour = to_visit[nc[1] * len(arr) + nc[0]]
            t_score = arr[nc[1]][nc[0]] + current[2]
            if t_score < g(neighbour):
                neighbour[1] = current
                neighbour[2] = g(current) + arr[neighbour[0][1]][neighbour[0][0]]
                neighbour.append(f(neighbour))
                if neighbour not in to_check:
                    to_check.append(neighbour)
        to_check.sort(key=lambda x: x[-1])

    return current

problem(1)
st = time.time()
solution = a_star_search(arr)

def get_path(node):
    current = node
    path = [current[0]]
    while current[1] != None:
        current = current[1]
        path.append(current[0])
    return path[::-1]

def print_path(arr, path):
    for j in range(len(arr)):
        string = ""
        for i in range(len(arr[j])):
            if [i, j] in path:
                string += "#"
            else:
                string += "."
        print(string)

def get_risk(arr, path):
    risk = 0
    for p in path:
        if p != [0, 0]:
            risk += arr[p[1]][p[0]]
    return risk

path = get_path(a_star_search(arr))
print(get_risk(arr, path), "{:.2f}s".format(time.time() - st))

problem(2)

def expand_arr(arr):
    new = []
    for i in range(5):
        for row in arr:
            new_row = []
            for j in range(5):
                for c in row:
                    val = (c + i + j) % 9
                    if val == 0:
                        val = 9
                    new_row.append(val)
            new.append(new_row)
    return new

expanded = expand_arr(arr)

st = time.time()
path = get_path(a_star_search(expanded))
print(get_risk(expanded, path), "{:.2f}s".format(time.time() - st))
