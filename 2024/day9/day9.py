with open("../day9/input.txt") as f:
    data = ''.join(f.read().splitlines())
    temp = []
    is_free = False
    curr = 0
    for num in data:
        num = int(num)
        if not is_free:
            for _ in range(num):
                temp.append(curr)
            curr += 1
            is_free = True
        else:
            for _ in range(num):
                temp.append(".")
            is_free = False

    left = 0
    right = len(temp) - 1

    while left < right:
        while left < right and temp[right] == ".":
            right -= 1
        while left < right and temp[left] != ".":
            left += 1
        if left < right:
            temp[left] = temp[right]
            temp[right] = "."
            left += 1
            right -= 1
    
    res = 0
    for i in range(len(temp)):
        if temp[i] != ".":
            res += i * int(temp[i])

    print(res)
