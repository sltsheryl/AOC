my_file = open("input.txt", "r")
vents = []
def remove_comma(str):
    new = str.replace(",", "")
    return new

def comma(str):
    x, y = str.split(",")
    return [int(x), int(y)]

for line in my_file:
    key, value = line.strip().split(" -> ")
    vents.append([comma(key), comma(value)])

start = map(lambda x: x[0], vents)
upper_bound = max(map(lambda x: x[0], start)) + 1
M = [[0] * upper_bound for _ in range(upper_bound)]

# counted = filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], vents)

for item in vents:
    if (item[0][0] == item[1][0]):
        start = min(item[0][1], item[1][1])
        end = max(item[0][1], item[1][1])
        for y in range(start, end + 1):
            M[y][item[0][0]] += 1

    elif (item[0][1] == item[1][1]):
        start = min(item[0][0], item[1][0])
        end = max(item[0][0], item[1][0])

        for x in range(start, end + 1):
            M[item[0][1]][x] += 1

    else:
        start_x = item[0][0]
        end_x = item[1][0]
        start_y = item[0][1]
        end_y = item[1][1]

        if start_x < end_x:
            if start_y < end_y:
                for i, j in zip(range(start_x, end_x + 1), range(start_y, end_y + 1)):
                    M[j][i] += 1
            else:
                for i,j in zip(range(start_x, end_x + 1), range(start_y, end_y - 1, -1)):
                    M[j][i] += 1
        elif start_x > end_x:
            if start_y < end_y:
                for i, j in zip(range(start_x, end_x - 1, -1), range(start_y, end_y + 1)):
                    M[j][i] += 1
            else:
                for i, j in zip(range(start_x, end_x - 1, -1), range(start_y, end_y - 1, -1)):
                    M[j][i] += 1


danger = 0
for lst in M:
    for num in lst:
        if num >= 2:
            danger += 1
print(danger)
