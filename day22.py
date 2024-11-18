from utils import get_input
from collections import namedtuple

Node = namedtuple('Node', ['size', 'used'])

grid = {}

for line in get_input(22).splitlines()[2:]:
    path, size, used, _, _ = line.split()
    name = path.split('/')[-1]
    x = int(name.split('-')[1].removeprefix('x'))
    y = int(name.split('-')[2].removeprefix('y'))
    grid[(x, y)] = Node(int(size.removesuffix('T')), int(used.removesuffix('T')))

width = max(x for x, _ in grid) + 1
height = max(y for _, y in grid) + 1

with open('scratch/day22.txt', 'w') as file:
    for y in range(height):
        if y > 0:
            print('    '.join(['   |   '] * width), file=file)
        row = []
        for x in range(width):
            node = grid[(x, y)]
            row.append('%3d/%-3d' % (node.used, node.size))
        print(' -- '.join(row), file=file)

empty = next(p for p in grid if grid[p].used == 0)
full = set(p for p in grid if grid[p].used > grid[empty].size)

print('1.', width * height - 1 - len(full))

for y in range(height):
    row = []
    for x in range(width):
        p = (x, y)
        if p == empty:
            row.append('_')
        elif p in full:
            row.append('#')
        else:
            row.append('.')
    print(' '.join(row))


