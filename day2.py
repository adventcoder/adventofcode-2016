from utils import get_input

dirs = { 'R': (2, 0), 'D': (0, 1), 'L': (-2, 0), 'U': (0, -1) }

def decode(lines, keypad):
    codes = []
    for line in lines:
        x, y = find(keypad, '5')
        for dir in line:
            dx, dy = dirs[dir]
            if valid(keypad, x + dx, y + dy):
                x, y = x + dx, y + dy
        codes.append(keypad[y][x])
    return ''.join(codes)

def get(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] != ' '

def find(grid, c):
    for y, line in enumerate(grid):
        for x in range(len(line)):
            if line[x] == c:
                return x, y

keypad1 = '''
1 2 3
4 5 6
7 8 9
'''.splitlines()

keypad2 = '''
    1
  2 3 4
5 6 7 8 9
  A B C
    D
'''.splitlines()

lines = get_input(2).splitlines()

print('1', decode(lines, keypad1))
print('2', decode(lines, keypad2))
