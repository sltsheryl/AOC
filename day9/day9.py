from functools import *
import sys
sys.setrecursionlimit(10000000)
my_file = open("input.txt", "r")

x = list(map(lambda x: list(x.strip("\n")), my_file.readlines()))
y = [[int(j) for j in i] for i in x]
rows = len(y)
cols = len(y[0])
low_points = []

neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for i in range(rows):
    for j in range(cols):
        target = y[i][j]
        state = True
        for row, col in neighbours:
            if 0 <= i + row < rows and 0 <= j + col < cols:
                if y[i + row][j + col] > target:
                    state = state and True
                else:
                    state = False
        if state == True:
            low_points.append([i, j])


def size(arr, i, j):
    M = [[0] * cols for _ in range(rows)]

    def helper(arr, i, j):
        nonlocal M

        if i < 0 or i >= rows:

            return 0
        elif j < 0 or j >= cols:

            return 0
        elif M[i][j] == 1:

            return 0

        elif arr[i][j] == 9:

            return 0
        else:

            M[i][j] = 1
            return 1 + helper(arr, i, j - 1) + helper(arr, i, j + 1) + helper(arr, i - 1, j) + helper(arr, i + 1, j)

    return helper(arr, i, j)


sizes = list(map(lambda x: size(y, x[0], x[1]), low_points))
sorted_sizes = sorted(sizes)
sorted_sizes.reverse()

result = 1
for i in range(3):
    result *= sorted_sizes[i]
print(result)
