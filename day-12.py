from lib import *

arr = file2arr("day-12.txt", lambda x: x.split('-'))

start = 'start'
end = 'end'
    
def isMinor(node):
    if node.islower() and not (node in [start, end]):
        return True
    return False

def getNodeCounts(path):
    count = {}
    for node in path:
        if node in count.keys():
            count[node] += 1
        else:
            count[node] = 1
    return count

def getNeighbours(node):
    return [n[0] for n in arr if n[1] == node and n[0] != start] + [n[1] for n in arr if n[0] == node and n[1] != start]

def isPathingFinished(paths):
    for path in paths:
        if path[-1] != end:
            return False 
    return True

def isValidUpdatedPath(node, count, minorRule=False):
    if node not in count.keys():
        return True
    if not isMinor(node):
        return True

    if not minorRule:
        # Cave must be minor, and can't appear more than once
        return False
    else:
        minor_count = 0
        for n in count.keys():
            if count[n] > 1 and isMinor(n):
                minor_count += 1
        if minor_count == 1:
            return False
        else:
            if count[n] > 1:
                return False
    return True

def findPaths(minorRule=False):
    finished = []
    paths = [[start]]

    while not isPathingFinished(paths):
        path = paths[-1]
        paths.remove(path)
        end_point = path[-1]
        if end_point == end:
            finished.append(path)
        else:
            count = getNodeCounts(path)
            for n in getNeighbours(end_point):
                if isValidUpdatedPath(n, count, minorRule=minorRule):
                    paths.append(path + [n])
        
    return len(finished + paths)


problem(1)

print(findPaths())

problem(2)

print(findPaths(minorRule=True))

