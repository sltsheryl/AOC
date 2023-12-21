def eachCard(line, cards):
    count = 0
    currCard = int(line.split(':')[0].split()[1])
    winningCards = line.split('|')[0].split(':')[1].split()
    allCards = line.split('|')[1].split()
    cards[currCard - 1] += 1
 
    for card in winningCards:
        if card in allCards:
            count += 1
    currCount = cards[currCard - 1]
    for i in range(count):
        cards[currCard + i] += 1 * currCount


with open('/Users/sheryl/aoc/2023/day4/input.txt') as f:
    s = f.read()
    lines = s.splitlines()
    cards = [0 for i in range(len(lines))]

    sum = 0
    for line in lines:
        eachCard(line, cards)
    
    for c in cards:
        sum += c
    print(sum)
