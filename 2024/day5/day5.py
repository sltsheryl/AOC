from collections import defaultdict
order = defaultdict(list)

def is_valid(ordering):
    for i in range(len(ordering)):
       curr =  ordering[i]
       for j in range(i+1, len(ordering)):
           if ordering[j] in order[curr]:
               continue
           if curr in order[ordering[j]]:
                return False
    return True

def get_middle_num(ordering):
    return ordering[len(ordering) // 2]

res = 0 
with open('../day5/input.txt') as f:
    for line in f:
        if line == '\n':
            break
        a, b = line.strip().split("|")
        order[int(a)].append(int(b))
    print(order)
    for line in f:
        ordering = list(map(lambda x: int(x), line.strip().split(",")))
        print(ordering)
        if is_valid(ordering=ordering):
            res += get_middle_num(ordering)

print(res)

