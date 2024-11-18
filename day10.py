from utils import get_input
from collections import defaultdict
from functools import cache
from operator import call
from math import prod

chips = defaultdict(lambda: defaultdict(list))

def chip(value):
    return lambda: value

def low_chip(type, id):
    return cache(lambda: min(values(type, id)))

def high_chip(type, id):
    return cache(lambda: max(values(type, id)))

def values(type, id):
    return map(call, chips[type][id])

for line in get_input(10).splitlines():
    match line.split():
        case [type, id, 'gives', 'low', 'to', low_type, low_id, 'and', 'high', 'to', high_type, high_id]:
            chips[low_type][low_id].append(low_chip(type, id))
            chips[high_type][high_id].append(high_chip(type, id))
        case ['value', value, 'goes', 'to', type, id]:
            chips[type][id].append(chip(value))

print('1.', next(id for id in chips['bot'] if sorted(values('bot', id)) == [17, 61]))
print('2.', prod(value for id in range(3) for value in values('output', id)))
