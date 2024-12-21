with open("../day9/input.txt") as f:
    data = ''.join(f.read().splitlines())
    free = []
    non_free = []
    for i in range(len(data)):
        if i % 2 == 0:
            non_free.append(int(data[i]))
        else:
            free.append(int(data[i]))
    
    free_pointer = 0
    non_free_pointer = len(non_free) - 1

    non_free_curr = 0
    
    temp = []

    while non_free_curr < non_free_pointer:
        for _ in range(non_free[non_free_curr]):
            temp.append(non_free_curr)
        non_free_curr += 1

        if free[free_pointer] >= non_free[non_free_pointer]:
            for _ in range(non_free[non_free_pointer]):
                temp.append(non_free_pointer)
            remaining = free[free_pointer] - non_free[non_free_pointer]
            for _ in range(remaining):
                temp.append(".")
            free_pointer += 1
            non_free_pointer -= 1
        else:
            for _ in range(free[free_pointer]):
                temp.append(".")
            non_free_pointer -= 1
    
    res = 0
    for i in range(len(temp)):
        if temp[i] != ".":
            res += i * int(temp[i])

    print(temp)
    print(res)
