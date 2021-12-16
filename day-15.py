from lib import *
import time
import math

arr = file2arr("day-15.txt", lambda x: [int(n) for n in x])

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

class Node:
    def __init__(self, coords, weight, prev=None,):
        self.coords = coords
        self.prev = prev
        self.weight = weight
    
    def update_node(self, weight):
        self.weight = min(self.weight, weight)

class NodeList:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_neighbours_in_list(self, arr, node):
        ncs = get_neighbours(arr, node.coords)
        finds = []
        cl = self.coords()
        for nc in ncs:
            if nc in cl:
                finds.append(self.nodes[cl.index(nc)])
        return finds
    
    def coords(self):
        return [n.coords for n in self.nodes]

    def find(self, coords):
        cl = self.coords()
        if coords in cl:
            return self.nodes[cl.index(coords)]

    def remove(self, coords):
        find = self.find(coords)
        if find != None:
            self.nodes.remove(find)

def find_path(arr):
    start = [0, 0]
    end = [len(arr[0]) - 1, len(arr) - 1]

    BIG = 10000000000

    visited = NodeList([])
    to_visit = NodeList([])

    pos = Node(start, 0)

    for n in get_neighbours(arr, pos.coords):
        to_visit.nodes.append(Node(n, BIG))

    while len(to_visit.nodes) > 0 and pos.coords != end:
        if len(visited.nodes) == 0:
            pos = Node(start, 0)
        else:
            # Position is the unvisited neighbour with the smallest weight
            candidates = [n for n in to_visit.nodes if n.weight != BIG]
            smallest = candidates[0]
            for n in candidates:
                if n.weight < smallest.weight:
                    smallest = n
            pos = smallest

        # Update lists
        to_visit.remove(pos.coords)
        visited.nodes.append(pos)

        for n in get_neighbours(arr, pos.coords):
            if n not in visited.coords():
                find = to_visit.find(n)
                point = arr[n[1]][n[0]]
                if find == None:
                    to_visit.nodes.append(Node(n, pos.weight + point))
                else:
                    node = find
                    node.update_node(pos.weight + point)
            

        # Update weights and prev values of neighbours

    return visited.find(end).weight, visited

def a_star_search(arr):
    BIG = 10000000000
    start = [0, 0]
    end = [len(arr[0]) - 1, len(arr) - 1]
    
    h = lambda a: 0

    def g(n):
        return n.weight
    
    def tentative_g(n):
        val = arr[n.coords[1]][n.coords[0]]
        current = n
        sum = 0
        while current.prev != None:
            current = current.prev
            sum += current.weight
        return sum + val
    
    def f(n):
        return g(n) + h(n.coords)
    
    def smallest(nodelist):
        nodes = nodelist.nodes
        smallest = nodes[0]

        for n in nodes:
            if f(n) < f(smallest):
                smallest = n

        return smallest

    to_visit = NodeList([])

    for j in range(len(arr)):
        for i in range(len(arr[j])):
            to_visit.nodes.append(Node([i, j], BIG))

    to_check = NodeList([Node(start, 0)])

    while len(to_check.nodes) != 0:
        current = smallest(to_check)

        if current.coords == end:
            return current

        to_check.nodes.remove(current)

        for nc in get_neighbours(arr, current.coords):
            neighbour = to_visit.nodes[nc[1] * len(arr) + nc[0]]
            t_score = tentative_g(neighbour)
            if t_score < g(neighbour):
                neighbour.prev = current
                neighbour.weight = g(current) + arr[neighbour.coords[1]][neighbour.coords[0]]
                if neighbour not in to_check.nodes:
                    to_check.nodes.append(neighbour)

        # for neighbour in to_visit.get_neighbours_in_list(arr, current):
        #     to_visit.remove(neighbour.coords)
        #     t_score = tentative_g(neighbour)
        #     if t_score < g(neighbour):
        #         neighbour.prev = current
        #         neighbour.weight = g(current) + arr[neighbour.coords[1]][neighbour.coords[0]]
        #         if neighbour not in to_check.nodes:
        #             to_check.nodes.append(neighbour)
    return current

problem(1)
st = time.time()
solution = a_star_search(arr)

def get_path(node):
    current = node
    path = [current.coords]
    while current.prev != None:
        current = current.prev
        path.append(current.coords)
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

print(get_risk(arr, get_path(solution)), "{:.2f}s".format(time.time() - st))

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
print(get_risk(expanded, get_path(a_star_search(expanded))), "{:.2f}s".format(time.time() - st))

# solution, visited = find_path(expanded)
# print(solution, "{:.2f}s".format(time.time() - st))
# # current = visited.find([len(expanded[0]) - 1, len(expanded) - 1])
# # path = current.coords

# # while current.prev != None:
# #     current = current.prev
# #     path.append(current.coords)

# # for coord in path[::-1]:
# #     print(coord)
