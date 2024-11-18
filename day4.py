from utils import get_input
from collections import Counter

def parse(name):
    i = name.index('[')
    groups = name[:i].split('-')
    return groups[:-1], int(groups[-1]), name[i+1:name.index(']',i+1)]

def calculate_checksum(groups, size):
    counts = Counter(''.join(groups))
    most_common = sorted(counts.keys(), key=lambda c: (-counts[c], c))
    return ''.join(most_common[:size])

def decrypt(groups, sector_id):
    words = []
    for group in groups:
        words.append(''.join(shift(c, sector_id) for c in group))
    return ' '.join(words)

def shift(c, n):
    if 'a' <= c <= 'z':
        return chr(ord('a') + (ord(c) - ord('a') + n) % 26)
    return c

rooms = []
for line in get_input(4).splitlines():
    groups, sector_id, checksum = parse(line)
    if calculate_checksum(groups, len(checksum)) == checksum:
        rooms.append((decrypt(groups, sector_id), sector_id))

print('1.', sum(sector_id for _, sector_id in rooms))
print('2.', next(sector_id for name, sector_id in rooms if 'northpole' in name))
