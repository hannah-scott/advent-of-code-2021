from lib import *
import time

arr = file2arr("day-14.txt")

def get_template_and_rules(arr):
    template = arr[0]

    rules = []
    for row in arr[2:]:
        rules.append(row.split(" -> "))

    return template, rules

template, rules = get_template_and_rules(arr)

def run_step(template, rules):
    pairs = []
    out = ""
    lookup = [n[0] for n in rules]

    for i in range(len(template) - 1):
        pairs.append(template[i:i+2])

    for i in range(len(pairs)):
        pair = pairs[i]
        if i == 0:
            # Don't repeat letters in the middle
            out += pair[0]
        if pair in lookup:
            out += rules[lookup.index(pair)][1]
        out += pair[1]
    return out

def add_to_count(el, c, value = 1):
    if el in c.keys():
        c[el] += value
    else:
        c[el] = value
    return c

def initialize_pair_count(template):
    pc = {}
    for i in range(len(template) - 1):
        pc = add_to_count(template[i:i+2], pc)
    return pc

def get_letter_counts(template):
    count = {}
    for n in template:
        if n in count.keys():
            count[n] += 1
        else:
            count[n] = 1
    return count

problem(1)

def run_steps(template, rules, n=10):
    for _ in range(n):
        template = run_step(template, rules)
        # print(initialize_pair_count(template))
    # print(get_letter_counts(template))
    values = get_letter_counts(template).values()

    return max(values) - min(values)

start = time.time()
print(run_steps(template, rules, n=10), "{:.2f}s".format(time.time() - start))

problem(2)

def debug_val(pc, key):
    if key in pc.keys():
        val = pc[key]
    else:
        val = 0
    return val

def run_pair_count_step(pc, rules):
    keys = list(pc.keys())
    lookup = [n[0] for n in rules]
    new = {}
    for key in keys:
        new[key] = pc[key]
    for key in keys:
        if key in [n[0] for n in rules]:
            # print("* {} -> {}".format(key, rules[lookup.index(key)][1]))
            found = rules[lookup.index(key)][1]

            val = debug_val(new, key[0] + found)
            new = add_to_count(key[0] + found, new, pc[key])
            # print("* \t{}: {} -> {}".format(key[0] + found, val, new[key[0] + found]))


            val = debug_val(new, found + key[1])
            new = add_to_count(found + key[1], new, pc[key])
            # print("* \t{}: {} -> {}".format(found + key[1], val, new[found + key[1]]))

            val = debug_val(new, key)

            new[key] -= pc[key]
            pc[key] = new[key]

            # print("* \t{}: {} -> {}".format(key, val, new[key]))
    for key in keys:
        if new[key] == 0:
            new.pop(key)
            pc.pop(key)
    return new

def get_lc_from_pc(pc):
    lc = {}
    for pair in pc:
        for letter in pair:
            lc[letter] = 0
    
    for pair in pc:
        for letter in pair:
            lc[letter] += pc[pair]

    return lc

def run_pair_count_steps(template, rules, n=10):
    pc = initialize_pair_count(template)
    first = template[0]
    last = template[-1]

    for _ in range(n):
        pc = run_pair_count_step(pc, rules)
        # print(pc)
    
    lc = get_lc_from_pc(pc)

    lc[first] += 1
    lc[last] += 1

    for l in lc.keys():
        lc[l] = int(lc[l] / 2)

    
    # print(lc)
    return max(lc.values()) - min(lc.values())
    
start = time.time()
print(run_pair_count_steps(template, rules, n=40), "{:.2f}s".format(time.time() - start))
