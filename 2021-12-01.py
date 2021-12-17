from lib import *

def inc_count(arr):
    inc_count = 0
    # For each row after the 0th, check if the measurement is larger than the previous one
    for i in range(1, len(arr)):
        if(arr[i] > arr[i-1]):
            # Increment a count if it is
            inc_count += 1
    return inc_count
 
def read_to_int(file):
    # Read file into array
    with open(file, "r") as f:
        # Remove newline and convert to int
        arr = [int(r.strip("\n")) for r in f.readlines()]
    return arr


problem(1)

# Read in file to array of integers
arr = read_to_int("day-1.txt")

# Print out the count
print(inc_count(arr))

problem(2)

# Calculate 3-point moving sum of the array
three_sum = lambda x, y, z: x + y + z

sum_arr = list(map(three_sum, arr[:-2], arr[1:-1], arr[2:]))

# Print out inc count
print(inc_count(sum_arr))