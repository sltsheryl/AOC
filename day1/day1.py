a_file = open("input.txt", "r")
xs = list(map(lambda x: int(x), a_file.readlines()))
length = len(xs)
def triple(xs):
    counter = 0
    for i in range(0, length - 3):
        a = xs[i] + xs[i + 1]  + xs[i + 2]
        b = xs[i + 1] + xs[i + 2]  + xs[i + 3]
        if (b > a):
            counter += 1
    return counter
print(triple(xs))
