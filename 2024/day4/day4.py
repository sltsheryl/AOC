grid = []
temp = []

with open('../day4/input.txt') as f:
    for line in f:
        temp.append(line.strip())
    grid = [['.' for i in range(len(temp[0]))] for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            grid[i][j] = temp[i][j]

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
word = "XMAS"
word_len = len(word)

def is_valid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def search_word(x, y, dx, dy):
    for k in range(word_len):
        nx, ny = x + k * dx, y + k * dy
        if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
            return False
    return True

def count_word_occurrences():
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in neighbors:
                if search_word(i, j, dx, dy):
                    count += 1
    return count

res = count_word_occurrences()
print(res)
