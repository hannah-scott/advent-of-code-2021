from lib import *

arr = file2arr("day-17.txt", lambda x: x[13:].split(", "))
target = list(map(lambda x: range(int(x[2:].split("..")[0]), int(x[2:].split("..")[1]) + 1), arr[0]))

# Pick one that works just to try to figure this out
velocity = [6, 9]


def run_simulation(velocity, target):
    pos = [0, 0]
    path = [[0,0]]

    while pos[0] <= max(target[0]) and pos[1] >= min(target[1]):
        pos[0] += velocity[0]
        pos[1] += velocity[1]

        path.append([pos[0], pos[1]])

        # Update velocity due to drag and gravity
        velocity[0] = max(0, velocity[0] - 1)
        velocity[1] -= 1

        if pos[0] in target[0] and pos[1] in target[1]:
            return path
    return False

def find_viable_y_velocities(target):
    viable = []
    for i in range(- 1 * (max(target[1]) - min(target[1])) * 10, (max(target[1]) - min(target[1])) * 10):
        pos = 0
        velocity = i
        while velocity >= min(target[1]):
            pos += velocity
            velocity -= 1
            if pos in target[1]:
                viable.append(i)
    return viable

def find_viable_x_velocities(target):
    viable = []
    for i in range(1, (max(target[0]) - min(target[0])) * 10):
        pos = 0
        velocity = i
        while velocity <= max(target[0]) and velocity > 0:
            pos += velocity
            velocity -= 1
            if pos in target[0]:
                viable.append(i)
    return viable


def find_max_viable_y_velocity(target):
    return max(find_viable_y_velocities(target))

def find_highest_point(velocity):
    y = velocity[1]
    point = 0
    while y + point > point:
        point = y + point
        y -= 1
    return point

problem(1)

print(find_highest_point([0, find_max_viable_y_velocity(target)]))

problem(2)

viable_x = list(set(find_viable_x_velocities(target)))
viable_y = list(set(find_viable_y_velocities(target)))

works = []

for x in viable_x:
    for y in viable_y:
        if run_simulation([x, y], target):
            works.append([x, y])

print(len(works))

