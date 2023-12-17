#!/opt/homebrew/bin/python3
num_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def eachLine(s):
    num = ""
    left = 0
    right = 0
    while right < len(s):
        for w in num_word:
            if w in s[left: right+1]:
                num += str(num_word.index(w) + 1)
                left = right

        if s[right].isdigit():
            num += s[right]
            left = right + 1
        
        right += 1
    res = ""
    res = num[0] + num[-1]
    print(num)

    return int(res)



with open('/Users/sheryl/aoc/day1/input.txt') as f:
    # read the file
    s = f.read()
    # get the sum of each line
    sum = 0
    for line in s.splitlines():
        sum += eachLine(line)
    print(sum)
