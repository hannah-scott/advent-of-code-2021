from lib import *

arr = file2arr("day-10.txt")

problem(1)

first = lambda x: [a[0] for a in x]
second = lambda x: [a[1] for a in x]

SYMBOLS = [
    ["(", ")"],
    ["[", "]"],
    ["{", "}"],
    ["<", ">"]
]

def get_score(c):
    SCORES = [
        [")", 3],
        ["]", 57],
        ["}", 1197],
        [">", 25137]
    ]
    if c in first(SCORES):
        return second(SCORES)[first(SCORES).index(c)]
    return 0

def check_line(line):
    open_chunks = []
    for c in line:
        if c in first(SYMBOLS):
            open_chunks.append(c)

        if c in second(SYMBOLS):
            index = second(SYMBOLS).index(c)
            if open_chunks[-1] == first(SYMBOLS)[index]:
                open_chunks = open_chunks[:-1]
            else:
                return False, c, None
    return True, None, open_chunks

def get_corrupt_score(arr):
    sum = 0
    for line in arr:
        valid, c, _ = check_line(line)
        if not valid:
            sum += get_score(c)
    return sum

print(get_corrupt_score(arr))

problem(2)

def get_autocomplete_scores(arr):
    SCORES = [
        [")", 1],
        ["]", 2],
        ["}", 3],
        [">", 4]
    ]
    scores = []
    for line in arr:
        valid, _, open_cs = check_line(line)
        if valid and len(open_cs) > 0:
            sum = 0
            auto = []
            for c in open_cs:
                auto.append(second(SYMBOLS)[first(SYMBOLS).index(c)])
            auto = auto[::-1]
            for a in auto:
                sum *= 5
                sum += second(SCORES)[first(SCORES).index(a)]
            scores.append(sum)
    return scores

def get_middle(arr):
    return arr[int((len(arr) - 1)/2)]

scores = get_autocomplete_scores(arr)
scores.sort()
print(get_middle(scores))