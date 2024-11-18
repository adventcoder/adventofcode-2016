from utils import get_input, astar
from functools import cache

seed = int(get_input(13))
goal = (31, 39)

@cache
def wall(x, y):
    return (x*x + 3*x + 2*x*y + y + y*y + seed).bit_count() & 1

def neighbours(p):
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and not wall(nx, ny):
            yield nx, ny

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

print('1.', astar((1,1), neighbours, lambda p: p == goal, lambda p: distance(p, goal)))

visited = set()
ps = {(1, 1)}
for _ in range(50):
    ps = { n for p in ps for n in neighbours(p) if n not in visited }
    visited.update(ps)
print('2.', len(visited))
