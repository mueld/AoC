import numpy as np

f = open("2022\Day6\InputData.txt", "r")
def p1(f):
    # forest = np.array([[]])
    forest = [[]]
    i = 0
    for line in f.read():
        forest.append()
        # forest.append(np.array([]))
        for n in line:
            forest[i].append(int(n))
        i+= 1
    visibletree = 0
    for i in range(0,len(forest)-1):
        for k in range(0, len(forest[i])):
            viewLeft = forest[i][:i]
            viewRight = forest[i][(i+1):]
            viewTop = forest[:i][k]
            viewButtom = forest[i+1:][i]
            tree = forest[i][k]
            if tree >= max(viewLeft) | tree >= max(viewRight) | tree >= max(viewTop) | tree >= max(viewButtom):
                visibletree += 1
    return visibletree
def p2(f):
    line = f.read()
    for i, k in enumerate(line):
        if len(set(line[i - 14 : i])) == 14:
            return i

print(p1(f))