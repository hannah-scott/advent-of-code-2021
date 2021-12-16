from lib import *

parse_fish = lambda x: list(map(int, x.split(",")))

with open("day-6.txt", "r") as f:
    fish = f.read()

problem(1)

initial = parse_fish(fish)

def run_simulation(fish, days):
    track = []
    for f in fish:
        track.append(f)
    for day in range(days + 1):
        if day > 0:
            for i in range(len(track)):
                track[i] -= 1
                if track[i] == -1:
                    track[i] = 6
                    track.append(8)
        # print("After {} days:\t{}".format(day, ",".join(map(str, track))))
    return len(track)

print(run_simulation(initial, 80))

problem(2)

# More efficient method

# If two fish have the same number of days to live, they are the same
# So let's make a dict

def init_fish(fish):
    initial = parse_fish(fish)
    fishes = {}
    for i in range(-1, 9):
        fishes[i] = 0
    for fish in initial:
        fishes[fish] += 1
    return fishes

def run_fast_simulation(fish, days):
    fishes = init_fish(fish)

    for _ in range(days):
        for i in range(9):
            fishes[i - 1] = fishes[i]
            fishes[i] = 0
        fishes[6] += fishes[-1]
        fishes[8] += fishes[-1]
        fishes[-1] = 0
    return fishes

def count_fishes(fishes):
    sum = 0
    for key in fishes.keys():
        sum += fishes[key]
    return sum

print(count_fishes(run_fast_simulation(fish, 256)))