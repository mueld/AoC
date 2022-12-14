f = open("2022\Day14\InputData.txt", "r")


def p1(f):
    grid = []
    input = f.read().replace(",", ".")
    for line in input.splitlines():
        underBound = min(float(path.strip()) for path in line.split("->"))
        upperBound = max(float(path.strip()) for path in line.split("->"))
    
    for path in f.readlines().split("->"):
        domain = [range(underBound,upperBound, 0.01)]
        for i,x in enumerate(path):
            if i < len(path) -1:
                p = range(path[i],path[i+1])
                overlap = domain - p
                for o in overlap:
                    for y, d in enumerate(domain):
                        if (o == d):
                          domain[y] = 1  
        grid.append(domain)
print(p1(f))
