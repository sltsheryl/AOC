my_file = open("test.txt", "r")
position = list(map(lambda x: int(x), my_file.readline().strip().split(',')))

def new_distance(y):
    sum = (y/2) * (2 + (y - 1))
    return sum

def distance(x):
    distance = 0
    for num in position:
        distance += new_distance(abs(num - x))
    return distance

lst = []
minimum = min(position)
maximum = max(position)
for i in range(minimum, maximum + 1):
    lst.append(distance(i))

minimum_value = min(lst)
minimum_index = lst.index(minimum_value)
value = minimum_index + minimum

print(minimum_value)
