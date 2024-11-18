from utils import get_input
from math import inf
import re

marker_pattern = r'\(([0-9]+)x([0-9]+)\)'

def decompress(s, max_depth):
    if max_depth == 0:
        return len(s)
    total = 0
    while m := re.search(marker_pattern, s):
        size = int(m.group(1))
        count = int(m.group(2))
        total += m.start() + decompress(s[m.end():m.end()+size], max_depth-1)*count
        s = s[m.end()+size:]
    total += len(s)
    return total

data = get_input(9).strip()
print('1.', decompress(data, 1))
print('2.', decompress(data, inf))
