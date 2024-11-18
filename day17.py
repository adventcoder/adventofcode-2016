from utils import get_input
import hashlib

dx = {'U':  0, 'D': 0, 'L': -1, 'R': 1}
dy = {'U': -1, 'D': 1, 'L':  0, 'R': 0}

passcode = get_input(17).strip()

def doors(path):
    hash = hashlib.md5((passcode + path).encode('ascii')).hexdigest()
    return [dir for dir, c in zip('UDLR', hash) if int(c, 16) >= 11]

shortest_path = None
longest_path = None
queue = [(0, 0, '')]
while queue:
    x, y, path = queue.pop()
    if x == 3 and y == 3:
        if shortest_path is None or len(path) < len(shortest_path):
            shortest_path = path
        if longest_path is None or len(path) > len(longest_path):
            longest_path = path
    else:
        for dir in doors(path):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                queue.append((nx, ny, path + dir))

print('1.', shortest_path)
print('2.', len(longest_path))
