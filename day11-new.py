from utils import get_input
import re
from collections import defaultdict
from itertools import combinations

elements = defaultdict(lambda: len(elements))

class Floor:
  def __init__(self, generators=0, microchips=0):
    self.generators = generators
    self.microchips = microchips

    def valid(self):
        return self.generators & ~self.microchips == 0

    def count(self):
        return self.generators.bit_count() + self.microchips.bit_count()

    def __iter__(self):
        for element in elements.values():
            if self.generators & (1 << element):
                yield element, 'generator'
            if self.microchips & (1 << element):
                yield element, 'microchip'

    def __add__(self, items):
        bits = { 'generator': self.generators, 'microchip': self.microchips }
        for element, type in items:
            bits[type] |= (1 << element)
        return Floor(bits['generator'], bits['microchip'])

    def __sub__(self, items):
        bits = { 'generator': self.generators, 'microchip': self.microchips }
        for element, type in items:
            bits[type] &= ~(1 << element)
        return Floor(bits['generator'], bits['microchip'])

def parse_floors(input):
    floors = [Floor() for _ in range(4)]
    for line in input.splitlines():
        tokens = re.sub(r'[.,]', '', line).split()
        floor = ['first', 'second', 'third', 'fourth'].index(tokens[1])
        for i in range(4, len(tokens) - 1):
            if tokens[i + 1] in ('generator', 'microchip'):
                element, type = tokens[i : i + 2]
                floors[floor] += [(elements.get(element.removesuffix('-compatible')), type)]
    return floors

def goal(state):
    elevator, floors = state
    return elevator == len(floors) - 1 and floors[-1].count() == len(elements) * 2

def step(state):
    elevator, floors = state
    for new_elevator in (elevator - 1, elevator + 1):
        if 0 <= new_elevator < len(floors):
            for items in combinations(floors[elevator].items, 2):
                new_floors = floors.copy()
                new_floors[elevator] -= items
                new_floors[new_elevator] += items
                if new_floors[elevator].valid() and new_floors[new_elevator].valid():
                    yield new_elevator, new_floors

def normalize(state):
    elevator, floors = state
    pairs = []
    for i, floor in enumerate(floors):
        for element, type in floor:
            pairs[element][type] = i
    return sorted(pairs)

def heuristic(state):
    elevator, floors = state
    counts = [floor.count() for floor in floors]
    return 0

def astar(start):
    pass

floors = parse_floors(get_input(11))
print('1.', astar(floors))
floors[0] += [item('elerium', 'generator'), item('elerium', 'microchip'), item('dilithium', 'generator'), item('dilithium', 'microchip')]
print('2.', astar(floors))
