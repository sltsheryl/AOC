
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
    currNum = ''
    isNum = False
    isBesideSymbol = False
    adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    for i in range(row):
        for j in range(col):
            if not matrix[i][j].isdigit():
                if isNum and isBesideSymbol:
                    print(currNum)
                    sum += int(currNum)
                currNum = ''
                isNum = False
                isBesideSymbol = False
            elif matrix[i][j].isdigit():
                currNum += matrix[i][j]
                isNum = True
                for a in adjacent:
                    x = i + a[0]
                    y = j + a[1]
                    if x >= 0 and x < row and y >= 0 and y < col:
                        if matrix[x][y] != '.' and not matrix[x][y].isdigit():
                            isBesideSymbol = True
    print(sum)

