from lib import *

problem(1)

# Read in file
with open("day-2.txt", "r") as f:
    arr = [r.strip("\n") for r in f.readlines()]

# Initialize current coordinates
pos = [0, 0]

def parse_dir(r):
    row = r.split(" ")
    row[1] = int(row[1])

    if row[0] == "forward":
        return [row[1], 0]
    elif row[0] == "up":
        return [0, -1 * row[1]]
    elif row[0] == "down":
        return [0, row[1]]
    
    # Shouldn't happen
    return [0, 0]

# For each row, parse the position and update current coordinates
arr_sum = lambda x, y: [x[0] + y[0], x[1] + y[1]]

for r in arr:
    d = parse_dir(r)
    pos = arr_sum(pos, d)

print(pos[0] * pos[1])

problem(2)

aim_pos = {
    "v": 0,
    "h": 0,
    "aim": 0
}

def parse_aim_dir(r):
    row = r.split(" ")
    row[1] = int(row[1])
    if row[0] == "forward":
        return {
            "len": row[1],
            "aim": 0
        }
    elif row[0] == "up":
        return {
            "len": 0,
            "aim": -1 * row[1]
        }
    elif row[0] == "down":
        return {
            "len": 0,
            "aim": row[1] 
        }
    # Shouldn't happen
    return {
        "len": 0,
        "aim": 0
    }

def aim_sum(pos, d):
    # Initialize and update aim direction
    out = pos
    out["aim"] += d["aim"]

    # Update position
    out["h"] += d["len"]
    out["v"] += d["len"] * out["aim"]

    return out

for r in arr:
    d = parse_aim_dir(r)
    aim_pos = aim_sum(aim_pos, d)

print(aim_pos["v"] * aim_pos["h"])