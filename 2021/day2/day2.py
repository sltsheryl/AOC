a_file = open("day2.txt", "r")
xs = list(map(lambda x: x.split(), a_file.readlines()))
length = len(xs)
x = 0
y = 0
aim = 0
for i in range(length):
    if (xs[i][0] == "forward"):
        x += int(xs[i][1])
        y += aim * int(xs[i][1])
    elif (xs[i][0] == "up"):
        aim -= int(xs[i][1])
    else:
        aim += int(xs[i][1])

print(x * y)
