

def eachGame(game):
    color = {}
    for g in game:
        colors = g.split(', ')
        for c in colors:
            curr_color = c.split()[1].strip(',')
            if curr_color in color:
                color[curr_color] = max(color[curr_color], int(c.split()[0].strip()))
            else:
                color[curr_color] = int(c.split()[0].strip())
    power = 1
    if 'red' in color:
        power *= color['red']
    if 'green' in color:
        power *= color['green']
    if 'blue' in color:
        power *= color['blue']
    return power

with open('/Users/sheryl/aoc/2023/day2/input.txt') as f:
    s = f.read()
    sum = 0
    index = 1
    for line in s.splitlines():
        game_id = index
        sets = line.split(';')[1:]
        sets.append(line.split(';')[0].split(':')[1])
        
        sets = [s.strip() for s in sets]
        sum += eachGame(sets)
    print(sum)
        


