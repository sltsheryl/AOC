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
    matches = re.finditer(pattern, content)
    pattern2 = r"do()"
    pattern3 = r"don't()"

    match_do = re.finditer(pattern2, content)

    match_dont = re.finditer(pattern3, content)

    
    do_start = list(map(lambda x: x.start(), match_do))
    dont_start = list(map(lambda x: x.start(), match_dont))
    
    is_enabled = True
    do_index = 0
    dont_index = 0
    
    for match in matches:
        curr_start = match.start()

        while do_index < len(do_start) and do_start[do_index] < curr_start:
            is_enabled = True
            do_index += 1
        while dont_index < len(dont_start) and dont_start[dont_index] < curr_start:
            is_enabled = False
            dont_index += 1

        if is_enabled and valid_mul(match.group()):
            res += eval_mul(match.group())

print(res)

  



