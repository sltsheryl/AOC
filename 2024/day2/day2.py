res = 0

def is_safe(lst):
    isIncreasing = False
    if lst[0] < lst[1]:
        isIncreasing = True
    for i in range(1, len(lst) - 1):
        if isIncreasing:
            if lst[i] > lst[i + 1]:
                return False
        else:
            if lst[i] < lst[i + 1]:
                return False
    for i in range(len(lst) - 1):
        if abs(lst[i + 1] - lst[i]) < 1 or abs(lst[i + 1] - lst[i]) > 3:
            return False
    return True

with open(file='../day2/input.txt', mode='r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lst = line.split(' ')
        nums = [int(num) for num in lst]
        if is_safe(nums):
            res += 1

print(res)
