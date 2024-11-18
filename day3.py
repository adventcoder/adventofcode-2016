from utils import get_input, ints

def possible(sides):
    return sum(sides) > 2*max(sides)

rows = [ints(line) for line in get_input(3).splitlines()]

print('1.', sum(possible(row) for row in rows))
print('2.', sum(possible(col[i:i+3]) for col in zip(*rows) for i in range(0, len(col), 3)))
