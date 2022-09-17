my_file = open("input.txt", "r")
life = my_file.readline().strip().split(",")
int_life = [int(num) for num in life]

fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in int_life:
    fish_count[fish] += 1
for i in range(256):
    fish_count.append(fish_count.pop(0))
    fish_count[6] += fish_count[8]


print(sum(fish_count))
