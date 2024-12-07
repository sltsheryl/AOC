
temp = []

def exit(i, j):
    return i < 0 or i >= rows or j < 0 or j >= cols

grid = []
originalDirection = (-1, -1)
originalPos = (-1, -1)

with open('../day6/input.txt') as f:
    for line in f:
        temp.append(line.strip())
    rows = len(temp)
    cols = len(temp[0])
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = temp[i][j]

    originalPos = (-1, -1)
    originalDirection = (-1, -1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^' or grid[i][j] == 'v' or grid[i][j] == '<' or grid[i][j] == '>':
                originalPos = (i, j)
                originalDirection = (0, 1) if grid[i][j] == '>' else (0, -1) if grid[i][j] == '<' else (-1, 0) if grid[i][j] == '^' else (1, 0)
                break
            
  

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  
def loop(i, j, grid, originalI, originalJ, originalDirection):
    currI = originalI
    currJ = originalJ
    currDirection = originalDirection
    visited = set()
    
    while True:
        newI = currI + currDirection[0]
        newJ = currJ + currDirection[1]
        print(newI, newJ)
        if exit(newI, newJ):
            return False
        
        if (newI, newJ, currDirection) in visited:
            return True
        
        visited.add((currI, currJ, currDirection))

        if grid[newI][newJ] == "#" or (newI == i and newJ == j):
            currDirection = directions[(directions.index(currDirection) + 1) % 4]
        
        else:
            currI = newI
            currJ = newJ

res = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            if loop(i, j, grid, originalPos[0], originalPos[1], originalDirection):
                res += 1

print(res)
        

    

