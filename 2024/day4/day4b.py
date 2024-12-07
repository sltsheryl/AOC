grid = []
temp = []

with open('../day4/input.txt') as f:
    for line in f:
        temp.append(line.strip())
    grid = [['.' for i in range(len(temp[0]))] for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            grid[i][j] = temp[i][j]


def valid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def counted(i, j):
    caseOne = valid(i - 1, j - 1) and grid[i - 1][j - 1] == 'M' and valid(i + 1, j + 1) and grid[i + 1][j + 1] == 'S'
    caseTwo = valid(i - 1, j - 1) and grid[i - 1][j - 1] == 'S' and valid(i + 1, j + 1) and grid[i + 1][j + 1] == 'M'
    caseThree = valid(i + 1, j - 1) and grid[i + 1][j - 1] == 'M' and valid(i - 1, j + 1) and grid[i - 1][j + 1] == 'S'
    caseFour = valid(i + 1, j - 1) and grid[i + 1][j - 1] == 'S' and valid(i - 1, j + 1) and grid[i - 1][j + 1] == 'M'
    return (caseOne or caseTwo) and (caseThree or caseFour)

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'A':
            if counted(i, j):
                res += 1

print(res)


