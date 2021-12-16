def problem(n):
    print("-" * 20)
    print("Problem {}".format(n))
    print("-" * 20)

def print_grid(grid, charset=False):
    for row in grid:
        string = ""
        for c in row:
            if charset:
                if c == 0:
                    string += "{}".format(charset[0])
                else:
                    string += "{}".format(charset[1])
            else:
                if c == 0:
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