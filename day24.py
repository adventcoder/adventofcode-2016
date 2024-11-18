from utils import get_input, astar
from functools import cache
from math import inf

grid = get_input(24).splitlines()

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def neighbours(p):
    x, y = p
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] != '#':
            yield nx, ny

size = max(int(c) for row in grid for c in row if c.isdigit()) + 1
all = (1 << size) - 1

points = [None] * size
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c.isdigit():
            points[int(c)] = (x, y)

matrix = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j] = astar(points[i], neighbours, lambda p: p == points[j], lambda p: distance(p, points[j]))
        matrix[j][i] = matrix[i][j]

@cache
def visit(start, end, visited = 0):
    visited |= 1 << start
    if visited == all:
        return matrix[start][end]
    best_distance = inf
    for i in range(size):
        if i != end and not visited & (1 << i):
            distance = matrix[start][i] + visit(i, end, visited)
            if distance < best_distance:
                best_distance = distance
    return best_distance

print('1.', min(visit(0, end, 1 << end) for end in range(size)))
print('2.', visit(0, 0))
