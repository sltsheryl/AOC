temp = []
with open("../day10/input.txt") as f:
    temp = [line.strip() for line in f]

grid = [list(line) for line in temp]

neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def valid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dfs(i, j):
    res = 0
    stack = [(i, j, int(grid[i][j]))]
    visited = set()
    while stack:
        x, y, val = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if val == 9:
            res += 1
        else:
            for dx, dy in neighbors:
             
                if valid(x + dx, y + dy) and grid[x + dx][y + dy].isdigit() and int(grid[x + dx][y + dy]) == val + 1:
                    stack.append((x + dx, y + dy, val + 1))      
    return res

output = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "0":
            output += dfs(i, j)

print(output)


