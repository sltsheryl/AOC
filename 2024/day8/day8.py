from collections import defaultdict
grid = []
with open("../day8/input.txt") as f:
    temp = []
    for line in f:
        temp.append(line.strip())
grid = [list(row) for row in temp]

dic = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]!= ".":
            dic[grid[i][j]].append((i,j))


def compute_antinodes(antenna_positions):
    antinodes = set()
    for i in range(len(antenna_positions)):
        for j in range(i):
            r_0, c_0 = antenna_positions[i]
            r_1, c_1 = antenna_positions[j]
            x_0, y_0 = 2 * r_1 - r_0, 2 * c_1 - c_0
            x_1, y_1 = 2 * r_0 - r_1, 2 * c_0 - c_1
            if 0 <= x_0 < len(grid) and 0 <= y_0 < len(grid[0]):
                antinodes.add((x_0, y_0))
            if 0 <= x_1 < len(grid) and 0 <= y_1 < len(grid[0]):
                antinodes.add((x_1, y_1))
    return antinodes


all_antinodes = set()
for freq, positions in dic.items():
    all_antinodes |= compute_antinodes(positions)

# Mark antinodes on the grid
for x, y in all_antinodes:
    grid[x][y] = "#"

# Write the output to a file
with open("output.txt", "w") as f:
    for row in grid:
        f.write("".join(row) + "\n")

print(len(all_antinodes))

