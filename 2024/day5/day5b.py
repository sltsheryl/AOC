from collections import defaultdict, deque
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

def topological_sort(ordering):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for i in range(len(ordering)):
        for j in range(i + 1, len(ordering)):
            if ordering[j] in order[ordering[i]]:
                graph[ordering[i]].append(ordering[j])
                in_degree[ordering[j]] += 1
            if ordering[i] in order[ordering[j]]:
                graph[ordering[j]].append(ordering[i])
                in_degree[ordering[i]] += 1

    zero_in_degree = deque([node for node in ordering if in_degree[node] == 0])
    topo_order = []

    while zero_in_degree:
        node = zero_in_degree.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)
    
    return topo_order

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
        if not is_valid(ordering=ordering):
            corrected = topological_sort(ordering)
            res += get_middle_num(ordering=corrected)

print(res)

