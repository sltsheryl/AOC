my_file = open("input.txt", "r")
lst = []
for line in my_file:
    lst.append(list(line.strip("\n")))

opened = ["{", "(", "[", "<"]
closed = ["}", ")", "]", ">"]
score = [3, 1, 2, 4]


def is_corrupt(line):
    acc = []
    for obj in line:
        if obj in opened:
            acc.append(obj)
        elif obj in closed:
            before = acc[-1]
            if obj == closed[opened.index(before)]:
                acc.pop()
            else:
                return True


def complete_lst(xs):
    result = []
    for opening in xs:
        ind = opened.index(opening)
        result.append(closed[ind])
    result.reverse()
    return result


def autocomplete(line):
    def scores(xs):
        result = 0
        for item in xs:
            result = result * 5 + score[closed.index(item)]
        return result

    store = []
    for obj in line:
        if obj in opened:
            store.append(obj)
        elif obj in closed:
            store.pop()
    return scores(complete_lst(store))


incomplete = list(filter(lambda x: is_corrupt(x) is None, lst))

all_scores = list(map(lambda x: autocomplete(x), incomplete))
all_scores.sort()

middle = all_scores[int(len(all_scores)/2)]
print(middle)
