import re
import fonts
import heapq
from math import inf

def get_input(day):
    with open(f'inputs/day{day}.txt') as file:
        return file.read()

def sgn(x):
    return (x >= 0) - (x <= 0)

def ints(s):
    return [int(s) for s in re.findall(r'-?[0-9]+', s)]

def ocr(grid, font=fonts.letters5x6, offset_x=0, offset_y=0):
    grid_width = max(map(len, grid))
    chars = []
    x = offset_x
    while x < grid_width:
        chars.append(font.lookup(grid, x, offset_y))
        x += font.glyph_width
    return ''.join(chars)

def astar(start, neighbours, goal, heuristic):
    queue = [(heuristic(start), start)]
    open = {start: 0}
    closed = set()
    while queue:
        _, curr = heapq.heappop(queue)
        if curr in closed:
            continue
        steps = open.pop(curr)
        closed.add(curr)
        if goal(curr):
            return steps
        for next in neighbours(curr):
            new_steps = steps + 1
            if new_steps < open.get(next, inf):
                open[next] = new_steps
                heapq.heappush(queue, (new_steps + heuristic(next), next))
