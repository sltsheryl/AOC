def eachCard(line):
    count = 0
    winningCards = line.split('|')[0].split(':')[1].split()
    allCards = line.split('|')[1].split()
    for card in winningCards:
        if card in allCards:
            count += 1
    if count == 0:
        return 0
    return pow(2, count - 1)


with open('/Users/sheryl/aoc/2023/day4/input.txt') as f:
    s = f.read()
    lines = s.splitlines()
    sum = 0
    for line in lines:
        sum += eachCard(line)
    print(sum)
