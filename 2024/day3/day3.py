import re

def valid_mul(s):
    print(s)
    if not s.startswith("mul(") or not s.endswith(")"):
        return False
    inside_bracket = s[4:-1]
    nums = inside_bracket.split(',')
    if len(nums) != 2:
        return False
    first = nums[0]
    second = nums[1]
    if first.isdigit() and second.isdigit():
        return True
    return False

def eval_mul(s):
    print(s)
    inside_bracket = s[4:-1]
    nums = inside_bracket.split(',')
    return int(nums[0]) * int(nums[1])

res = 0
with open(file='../day3/input.txt', mode='r') as f:
    content = f.read().splitlines()
    content = ''.join(content)
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, content)

    for match in matches:
        if valid_mul(match):
            res += eval_mul(match)

print(res)

  



