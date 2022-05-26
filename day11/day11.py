def helper(time, arr):
    flashes = 0

    def step(arr):
        nonlocal flashes
        zero = []
        col = len(arr[0])
        row = len(arr)
        for i in range(row):
            for j in range(col):
                arr[i][j] += 1
        print(arr)
        for i in range(row):
            for j in range(col):
                if arr[i][j] > 9:
                    zero.append((i, j))
                    
                    flash(arr, i, j)
            
                    flashes += 1
        print(arr)
                    neighbor = neighboring(arr, i, j)
                    for a, b in neighbor:
                        if arr[a][b] > 9:
                            zero.append((a, b))
                            flash(arr, a, b)
                            flashes += 1
        
        print(zero, "zero")
        for x, y in zero:
            arr[x][y] = 0
        print(arr)
    for i in range(time):
        step(arr)
        print(flashes, "once")
    print(flashes)


def neighboring(arr, r, c):
    col = len(arr[0])
    row = len(arr)
    neighbor = [-1, 0, 1]
    acc = []
    for i in neighbor:
        for j in neighbor:
            if i + r >= 0 and i + r < row and j + c >= 0 and j + c < col:
                acc.append((i + r, c + j))
    for item in acc:
        if item[0] == r and item[1] == c:
            acc.remove(item)
    return acc


def flash(arr, r, c):
    to_add = neighboring(arr, r, c)
    for i, j in to_add:
        arr[i][j] += 1


my_file = open("day11.txt", "r")
lines = my_file.readlines()
new_lines = []
for line in lines:
    new_lines.append(list(line.strip("\n")))

new_lines = [[int(j) for j in i] for i in new_lines]


helper(2, new_lines)


# a = [[2, 2, 2, 2, 2], [2, 10, 10, 10, 2], [2, 10, 2, 10, 2], [2, 10, 10, 10, 2], [2, 2, 2, 2, 2]]
# flash(a, 1, 1)
# print(a)
