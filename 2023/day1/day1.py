#!/opt/homebrew/bin/python3
def eachLine(s):
    num = ""
    for c in s:
        # if c is a digit
        if c.isdigit():
            num += c
    res = num[0] + num[-1]
    return int(res)


with open('/Users/sheryl/aoc/day1/input.txt') as f:
    # read the file
    s = f.read()
    # get the sum of each line
    sum = 0
    for line in s.splitlines():
        sum += eachLine(line)
    print(sum)

