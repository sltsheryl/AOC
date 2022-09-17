a_file = open("input.txt", "r")
xs = list(map(lambda x: list(x), a_file.readlines()))
list(map(lambda x: x.pop(), xs))

def complement(x):
    if x == '0':
        return '1'
    else:
        return '0'

def common(xs):
    zeros = 0
    ones = 0
    for byte in xs:
        if (byte == '0'):
            zeros += 1
        else:
            ones += 1
    if (ones > zeros):
        return '1'
    elif (zeros > ones):
        return '0'
    else:
        return 'none'

def most_common(xs):
    length = len(xs)
    a =[]
    for i in range(length):
        a = list(map(lambda x: x[0], xs))
    return common(a)

def o2(xs):
    store = []
    def helper(xs):
        if len(xs) == 1:
            store.extend(xs[0])
            return store
        else:
            first = most_common(xs)
            if first == 'none':
                store.append("1")
                xs = [i[1:] for i in xs if i[0] == '1']
                return helper(xs)
            else:

                store.append(first)
                xs = [i[1:] for i in xs if i[0] == first]
                return helper(xs)
    return helper(xs)

def co2(xs):
    store = []
    def helper(xs):
        if len(xs) == 1:
            store.extend(xs[0])
            return store
        else:
            first = most_common(xs)
            real = complement(first)
            if first == 'none':

                store.append("0")
                xs = [i[1:] for i in xs if i[0] == '0']
                return helper(xs)
            else:
                store.append(real)
                xs = [i[1:] for i in xs if i[0] == real]
                return helper(xs)
    return helper(xs)


o2_int = int(''.join(o2(xs)), 2)
co2_int = int(''.join(co2(xs)), 2)
print(o2_int * co2_int)
