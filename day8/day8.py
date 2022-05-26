from functools import *
my_file = open("input.txt", "r")
dict = {}
for line in my_file:
    key, value = line.strip().split(" | ")
    dict[key] = value


def inside(xs, ys):
    state = True
    for item in xs:
        if item not in ys:
            state = state and False
        else:
            state = state and True
    return state


def decode(xs):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = dict.fromkeys(keys)
    for elem in xs:
        if len(elem) == 2:
            d[1] = elem
        elif len(elem) == 3:
            d[7] = elem
        elif len(elem) == 4:
            d[4] = elem
        elif len(elem) == 7:
            d[8] = elem
    for elem in xs:
        if len(elem) == 6:
            if inside(d[4], elem):
                d[9] = elem
            elif inside(d[7], elem):
                d[0] = elem
            else:
                d[6] = elem
    for elem in xs:
        if len(elem) == 5:
            if inside(d[7], elem):
                d[3] = elem
            elif inside(elem, d[6]):
                d[5] = elem
            else:
                d[2] = elem
    return d


def match(ys, d):
    output = []
    for item in ys:
        for key, value in d.items():
            if inside(item, value) and len(item) == len(value):
                output.append(key)
    a_string = "".join(map(lambda x: str(x), output))
    return int(a_string)


sum = 0
for key, value in dict.items():
    xs = key.split(" ")
    ys = value.split(" ")
    new_d = decode(xs)
    result = match(ys, new_d)
    sum += result

print(sum)


# nums = list(reduce(lambda x, y: x + y, map(lambda x: x.split(" "), values)))
# letters = []
# print(dict)
# for num in nums:
#     if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
#         counter += 1
# print(counter)
