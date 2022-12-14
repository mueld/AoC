from math import prod
import numpy as np

f = open("2022\Day8\InputData.txt", "r")
def p1(f):
    
    grid = f.read().splitlines()
    visibleTrees =  0
    for ri, row in enumerate(grid):
      for ti, tree in enumerate(grid[ri]):
        visibleTrees += (
          all(grid[ri][j] < tree for j in range(0, ti))
          or all(grid[ri][j] < tree for j in range(ti+1, len(row)))
          or all(grid[j][ti] < tree for j in range(0,ri))
          or all(grid[j][ti] < tree for j in range(ri + 1, len(row)))
        )
    return visibleTrees

def p2(f):
    grid = f.read().splitlines()
    ans = []

    for gi, row in enumerate(grid):
        for gk, tree in enumerate(row):
          ans.append([0, 0, 0, 0])
          k = len(ans)-1
          # view left
          for i in range(gk -1, -1, -1):
            ans[k][0] += 1
            if grid[gi][i] >= tree: 
              break

            # view right
          for i in range(gk + 1, len(row)):
            ans[k][1] += 1
            if grid[gi][i] >= tree: 
              break 

          # view top
          for i in range(gi -1, -1, -1):
            ans[k][2] += 1
            if grid[i][gk] >= tree: 
              break

          # view buttom
          for i in range(gi + 1, len(grid)):
            ans[k][3] += 1
            if grid[i][gk] >= tree: 
              break
          
    return max(prod(x) for x in ans)
print(p2(f))