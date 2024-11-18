from utils import get_input, ocr

def rotate(vals, n):
    n %= len(vals)
    return vals[-n:] + vals[:-n]

screen = [['.'] * 50 for _ in range(6)]
for line in get_input(8).splitlines():
    tokens = line.split()
    if tokens[0] == 'rect':
        w, h = map(int, tokens[1].split('x'))
        for y in range(h):
            for x in range(w):
                screen[y][x] = '#'
    elif tokens[0] == 'rotate':
        i = int(tokens[2][2:])
        n = int(tokens[4])
        if tokens[1] == 'row':
            screen[i] = rotate(screen[i], n)
        elif tokens[1] == 'column':
            vals = [row[i] for row in screen]
            for row, val in zip(screen, rotate(vals, n)):
                row[i] = val

print('1.', sum(c == '#' for row in screen for c in row))
print('2.', ocr(screen))
