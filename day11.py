from utils import get_input
from collections import namedtuple
import re
import heapq

Item = namedtuple('Item', ['generator', 'microchip'])

def parse_items(input):
    generators = {}
    microchips = {}
    for line in input.splitlines():
        tokens = re.sub(r'[.,]', '', line).split()
        floor = ['first', 'second', 'third', 'fourth'].index(tokens[1])
        for i in range(4, len(tokens) - 1):
            element, type = tokens[i : i + 2]
            if type == 'generator':
                generators[element] = floor
            elif type == 'microchip':
                microchips[element.removesuffix('-compatible')] = floor
    items = []
    for element in generators.keys() | microchips.keys():
        items.append(Item(generators[element], microchips[element]))
    return items

def valid(items):
    mask = 0
    for item in items:
        mask |= 1 << item.generator
    for item in items:
        # unprotected chip and floor contains generators
        if item.generator != item.microchip and mask & (1 << item.microchip):
            return False
    return True

def moves(items, floor, new_floor):
    for i, item in enumerate(items):
        if item.generator == floor:
            yield items[:i] + [Item(new_floor, item.microchip)] + items[i+1:]
        if item.microchip == floor:
            yield items[:i] + [Item(item.generator, new_floor)] + items[i+1:]

def next_states(state):
    elevator, items = state
    for new_elevator in (elevator - 1, elevator + 1):
        if 0 <= new_elevator < 4:
            for new_items1 in moves(items, elevator, new_elevator):
                if valid(new_items1):
                    yield new_elevator, new_items1
                for new_items2 in moves(new_items1, elevator, new_elevator):
                    if valid(new_items2):
                        yield new_elevator, new_items2

def normalize(state):
    elevator, items = state
    return (elevator, bytes(sorted((item.generator << 2) | item.microchip for item in items)))

# for the heuristic calculate the minimum number of steps ignoring the chip frying constraint
def heuristic(state):
    elevator, items = state

    # count of items on each floor
    counts = [0] * 4
    for item in items:
        counts[item.generator] += 1
        counts[item.microchip] += 1

    # lowest floor with an item
    min_floor = next(floor for floor, count in enumerate(counts) if count > 0)

    # bring one item from current floor down to lowest floor to power elevator
    counts[elevator] -= 1
    counts[min_floor] += 1
    steps = elevator - min_floor

    while min_floor < 3:
        # takes n-1 steps to lift all items up one floor
        steps += max(counts[min_floor] - 1, 1)
        counts[min_floor + 1] += counts[min_floor]
        min_floor += 1

    return steps

def goal(state):
    elevator, items = state
    return elevator == 3 and all(item.generator == elevator and item.microchip == elevator for item in items)

# this would be faster with a bucket based priority queue
def astar(start):
    costs = { normalize(start): 0 }
    open = [(heuristic(start), start)]
    closed = set()
    while open:
        _, state = heapq.heappop(open)
        key = normalize(state)
        if goal(state):
            return costs[key]
        if key not in closed:
            closed.add(key)
            for new_state in next_states(state):
                new_cost = costs[key] + 1
                new_key = normalize(new_state)
                if new_key in costs and new_cost >= costs[new_key]:
                    continue
                costs[new_key] = new_cost
                heapq.heappush(open, (new_cost + heuristic(new_state), new_state))

items = parse_items(get_input(11))
print('1.', astar((0, items)))
items.extend([Item(0, 0), Item(0, 0)])
print('2.', astar((0, items)))
