from lib import *

splitint = lambda x: [int(s) for s in x.split(",")]
arr = file2arr("2021-12-07.txt", splitint)[0]

arr.sort()

problem(1)

min = [-1, 1000000000]

for i in range(arr[0], arr[-1]):
    sum = 0
    for r in arr:
        sum += abs(r - i)
    if sum < min[1]:
        min = [i, sum]

print(min[1])

problem(2)

min = [-1, 1000000000]

# Fuel consumption is a triangle number: n(n+1)/2, where
# n is distance to be travelled
triangle = lambda x, y: int(abs(x - y) * (abs(x - y) + 1) / 2)

for i in range(arr[0], arr[-1]):
    sum = 0
    for r in arr:
        sum += triangle(r, i)
    if sum < min[1]:
        min = [i, sum]

print(min[1])