with open("../day11/input.txt") as f:
    stones = f.readline().strip().split()

memo = {}

def get_num(stone, set_times):
    if (stone, set_times) in memo:
        return memo[(stone, set_times)]
    
    if set_times == 0:
        return 1
    
    if stone == 0:
        result = get_num(1, set_times - 1)
    elif len(str(stone)) % 2 == 0:
        left_half = int(str(stone)[:len(str(stone)) // 2])
        right_half = int(str(stone)[len(str(stone)) // 2:])
        result = get_num(left_half, set_times - 1) + get_num(right_half, set_times - 1)
    else:
        result = get_num(stone * 2024, set_times - 1)
    
    memo[(stone, set_times)] = result
    return result

res = 0
for stone in stones:
    res += get_num(int(stone), 75)

print(res)
