f = open("2022\Day13\InputData.txt", "r")

def compare(x,y):
    if isinstance(x,int) & isinstance(y,int):
        return x-y

    if isinstance(x, list) & isinstance(y,list):
        for a,b in zip(x,y):
            result = compare(a,b)
            if result:
                return result
        return len(x)-len(y)

    if isinstance(x, list):
        return compare(x,[y])
    
    if isinstance(y,list):
        return compare([x],y)

    assert False

def p1(f):
    pairs = [[eval(p) for p in pair.splitlines()] for pair in f.read().split("\n\n")]
    return sum(i+1 for i,(x,y) in enumerate(pairs) if compare(x,y)<0)

print(p1(f))
