from collections import deque
import numpy as np

f = open("2022\Day11\InputData.txt", "r")

def possibleNextPos(x,y):
    return (x-1,y),(x,y-1),(x+1,y),(x,y+1)

def p1(f):
    grid = {
        (i, j): x
        for i, row in enumerate(f.read().splitlines())
        for j, x in enumerate(row)
    }
    
    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")
    
    grid[start] = "a"
    grid[end] = "z"

    steps = {}
    queue = deque([(0, start)])

    while(len(queue) > 0):
        c,p = queue.popleft()
        if p in steps:
            continue
        steps[p] = c
        currentField = grid[p]
        for step in possibleNextPos(*p):
            nextField = grid.get(step,"~")
            if ord(nextField) - ord(currentField) > 1:
                continue
            queue.append((c + 1,step))
   
    return steps[end]



def p2(f):
    grid = {
        (i, j): x
        for i, row in enumerate(f.read().splitlines())
        for j, x in enumerate(row)
    }
    
    starts = {k for k, v in grid.items() if v == "a"}
    end = next(k for k, v in grid.items() if v == "E")
    
    grid[end] = "z"

    steps = {}
    queue = deque([(0, s)for s in starts] )

    while(len(queue) > 0):
        c,p = queue.popleft()
        if p in steps:
            continue
        steps[p] = c
        currentField = grid[p]
        for step in possibleNextPos(*p):
            nextField = grid.get(step,"~")
            if ord(nextField) - ord(currentField) > 1:
                continue
            queue.append((c + 1,step))
   
    return steps[end]

print(p2(f))