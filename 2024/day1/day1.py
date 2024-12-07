import os
from collections import defaultdict
print("Current working directory:", os.getcwd())

# Check if the file exists
file_path = '../day1/input.txt'
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    a = []
    b = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x, y = line.split('   ')
            a.append(int(x))
            b.append(int(y))
    dic = defaultdict(int)
    res = 0
    for num in b:
        dic[num] += 1
    for num in a:
        res += num * dic[num]

    print(res)
