
temp = []

def exit(i, j):
    return i < 0 or i >= rows or j < 0 or j >= cols

with open('../day6/input.txt') as f:
    for line in f:
        temp.append(line.strip())
    rows = len(temp)
    cols = len(temp[0])
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = temp[i][j]
    visited = set() 
    originalPos = (-1, -1)
    originalDirection = (-1, -1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^' or grid[i][j] == 'v' or grid[i][j] == '<' or grid[i][j] == '>':
                originalPos = (i, j)
                originalDirection = (0, 1) if grid[i][j] == '>' else (0, -1) if grid[i][j] == '<' else (-1, 0) if grid[i][j] == '^' else (1, 0)
                break
            
    visited.add(originalPos)
    currPos = originalPos
    currDirection = originalDirection

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    print(grid)

    while True:
        newI = currPos[0] + currDirection[0]
        newJ = currPos[1] + currDirection[1]

        if exit(newI, newJ) or grid[newI][newJ] == " ":
            break

        if grid[newI][newJ] == "#":
            currDirection = directions[(directions.index(currDirection) + 1) % 4]
        
        else:
            currPos = (newI, newJ)
            visited.add((newI, newJ))

print(len(visited))
        

    

