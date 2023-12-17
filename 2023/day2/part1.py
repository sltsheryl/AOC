RED = 12
GREEN = 13
BLUE = 14

def eachSet(s):
    s_list = s.split(',')
    print(s_list)
    color = {}
    red = 0
    green = 0
    blue = 0
    for i in s_list:
        color[i.split()[1]] = int(i.split()[0])
    if 'red' in color:
        red = color['red']
    if 'green' in color:
        green = color['green']
    if 'blue' in color:
        blue = color['blue']
    print(color)
    if red <= RED and green <= GREEN and blue <= BLUE:
        return True
    return False

with open('/Users/sheryl/aoc/2023/day2/input.txt') as f:
    s = f.read()
    sum = 0
    index = 1
    for line in s.splitlines():
        game_id = index
        sets = line.split(';')[1:]
        sets.append(line.split(';')[0].split(':')[1])
        sets = [s.strip() for s in sets]
        valid_game = True
        for s in sets:
            if not eachSet(s):
                valid_game = False
                break
        if valid_game:
            print(game_id)
            sum += game_id
        index += 1
    print(sum)


