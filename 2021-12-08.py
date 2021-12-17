from lib import *

# Get input
with open("2021-12-08.txt", "r") as f:
    inputs = [n.strip().split(" | ") for n in f.readlines()]


problem(1)

count_of_unique_lengths = 0

for input in inputs:
    code = input[1].split(" ")
    for s in code:
        if len(s) in [2, 3, 4, 7]:
            count_of_unique_lengths += 1

print(count_of_unique_lengths)

problem(2)

def count_arr(arr, el):
    sum = 0
    for e in arr:
        if el == e:
            sum += 1
    return sum

def decode_input(input):
    NUMBERS = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }

    encoded = {}

    numbers = input[0].split(" ")
    pairs_off_by_1 = []

    for number in numbers:
        if len(number) in [2, 3, 4, 7]:
            cand = [n for n in NUMBERS.keys() if len(NUMBERS[n]) == len(number)][0]
            encoded[cand] = number
        if len(number) == 5:
            # Three pairs of numbers have representations that
            # differ by only one light:
            # - 3 and 9
            # - 5 and 6
            # - 5 and 9
            for other in numbers:
                if len(other) == 6:
                    matched = True
                    for l in number:
                        if l not in other:
                            matched = False
                    if matched:
                        pairs_off_by_1.append([number, other])
                    
    first = [pair[0] for pair in pairs_off_by_1]
    second = [pair[1] for pair in pairs_off_by_1]
    for elem in list(set(first)):
        if count_arr(first, elem) > 1:
            encoded[5] = elem
        else:
            encoded[3] = elem
    for elem in list(set(second)):
        if count_arr(second, elem) > 1:
            encoded[9] = elem
        else:
            encoded[6] = elem
    
    for number in numbers:
        if number not in encoded.values():
            if len(number) == 5:
                encoded[2] = number
            if len(number) == 6 :
                encoded[0] = number
    return encoded

def get_key(d, v):
    for key, value in d.items():
        if v == value:
            return key
    return

sum = 0
for input in inputs:
    encoded = decode_input(input)

    for key in encoded.keys():
        encoded[key] = [l for l in encoded[key]]
        encoded[key].sort()
        encoded[key] = "".join(encoded[key])
    
    sorted = []
    for number in input[1].split(" "):
        c = [l for l in number]
        c.sort()
        c = "".join(c)
        sorted.append(c)

    out = ""
    for number in sorted:
        out += str(get_key(encoded, number))
    sum += int(out)
print(sum)