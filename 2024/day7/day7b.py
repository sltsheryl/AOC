def possible(nums, target):
    def helper(i, prev):
        if i == len(nums):
            return prev == target
        if prev <= target:
            return helper(i + 1, prev + nums[i]) or helper(i + 1, prev * nums[i]) or helper(i + 1, int(str(prev) + str(nums[i])))
        return False
    return helper(0, 0)

res = 0

with open("../day7/input.txt") as f:
    for line in f:
        left, right = line.strip().split(":")
        target = int(left)
        nums = list(map(lambda x: int(x), right.strip().split(" ")))
        if possible(nums, target):
            res += target

print(res)
