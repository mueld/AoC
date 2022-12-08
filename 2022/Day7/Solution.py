from collections import defaultdict
from pathlib import Path


# def p1(f):
#     cwd = Path("/")
#     dirs = defaultdict(int)

#     for line in f.read().splitlines():
#         match line.split():
#             case ["$", "cd", newdir]:
#                 cwd = cwd / newdir
#                 cwd = cwd.resolve()
#             case [size, _] if size.isdigit():
#                 size = int(size)
#                 for path in [cwd, *cwd.parents]:
#                     dirs[path] += size

#     return sum(x for x in dirs.values() if x <= 100000)
cwd = root = {}
stack = []
# f = open("2022\Day7\InputData.txt", "r")
for line in open("2022\Day7\InputData.txt", "r"):
    line = line.strip()
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                cwd = root
                stack = []
            elif dir == "..":
                cwd = stack.pop()
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]
    else:
        x, y = line.split()
        if x == "dir":
            if y not in cwd:
                cwd[y] = {}
        else:
            cwd[y] = int(x)

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

t = size() - 40_000_000

def solve(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans

print(solve())
