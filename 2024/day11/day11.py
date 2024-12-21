with open("../day11/input.txt") as f:
    stones = f.readline().strip().split()


def get_num(stone, set_times):
    stack = [([stone], 0)]
    while stack:
        stones, times = stack.pop()
        if times == set_times:
            return len(stones)
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left_half = str(stone)[:len(str(stone)) // 2]
                right_half = str(stone)[len(str(stone)) // 2:]
                new_stones.append(int(left_half))
                new_stones.append(int(right_half))
            else:
                new_stones.append(stone * 2024)
        stack.append((new_stones, times + 1))
    return -1
 
res = 0
for stone in stones:
    res += get_num(int(stone), 25)

print(res)
