import numpy as np

f = open("2022\Day6\InputData.txt", "r")
def p1(f):
    line = f.read()
    for i, k in enumerate(line):
        if len(set(line[i - 4 : i])) == 4:
            return i

def p2(f):
    line = f.read()
    for i, k in enumerate(line):
        if len(set(line[i - 14 : i])) == 14:
            return i

print(p2(f))