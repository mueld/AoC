from collections import defaultdict
from pathlib import Path

f = open("2022\Day7\InputData.txt", "r")
def p1(f):
  cwd = Path("/")
  dirc = defaultdict(int)
  for line in f.read().splitlines():
    splitedline =line.split()
    match splitedline:
      case ["$","cd", newdic]:
        cwd = cwd.joinpath(newdic)
        cwd = cwd.resolve()
      case [size, _] if(size.isdigit()):
        size = int(size)
        for path in [cwd, *cwd.parents]:
            dirc[path] += size
  size = 0

p1(f)