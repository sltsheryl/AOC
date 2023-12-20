#!/opt/homebrew/bin/python3
with open('/Users/sheryl/aoc/2023/day3/input.txt') as f:
    s = f.read()
    grid = []
    for line in s.splitlines():
        grid.append(line)
    row = len(grid)
    col = len(grid[0])
    matrix = [['a' for x in range(col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            matrix[i][j] = grid[i][j]
    sum = 0
    count = 0
    currNum = ''
    gearRatio = 1
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    visited = [[False for x in range(col)] for y in range(row)]

    res = [0, 0]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '*':
                for a in adjacent:
                    
                    x = i + a[0]
                    y = j + a[1]
                    if x >= 0 and x < row and y >= 0 and y < col:
                        if matrix[x][y].isdigit() and not visited[x][y]:
                            visited[x][y] = True
                            currNum = matrix[x][y]
                            start = y-1
                            end = y+1
                            while start >= 0 and start < col and matrix[x][start].isdigit():
                                currNum = matrix[x][start] + currNum
                                visited[x][start] = True
                                start -= 1
                            while end >= 0 and end < col and matrix[x][end].isdigit():
                                currNum += matrix[x][end]
                                visited[x][end] = True
                                end += 1
                            res[count] = currNum
                            count += 1

                            if count == 2:
        
                                gearRatio = int(res[0]) * int(res[1])
                                sum += gearRatio
                                count = 0
                                currNum = ''
                                gearRatio = 1
                                break
                count = 0
                currNum = ''
                gearRatio = 1

                            

          
    print(sum)

    
              