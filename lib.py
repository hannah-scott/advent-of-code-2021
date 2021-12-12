def problem(n):
    print("-" * 20)
    print("Problem {}".format(n))
    print("-" * 20)

def print_grid(grid, dot = False):
    for row in grid:
        string = ""
        for c in row:
            if c == 0 and dot == True:
                string += ". "
            else:
                string += "{} ".format(c)
        print(string)


def file2arr(fname, fn=None):
    with open(fname, "r") as f:
        arr = [n.strip() for n in f.readlines()]
    
    if fn != None:
        return list(map(fn, arr))
    return arr