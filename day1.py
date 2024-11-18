from utils import get_input
from collections import Counter

dirs = { 'L': 1j, 'R': -1j }
dir = 1
path = [0]
for step in get_input(1).strip().split(', '):
    dir *= dirs[step[0]]
    for _ in range(int(step[1:])):
        path.append(path[-1] + dir)

def distance(pos):
    return int(abs(pos.real) + abs(pos.imag))

print('1.', distance(path[-1]))

counts = Counter(path)
print('2.', distance(next(pos for pos in path if counts[pos] > 1)))
