from utils import get_input

code = [line.split() for line in get_input(25).splitlines()]

x = int(code[1][1]) * int(code[2][1])

def ceil_pattern(x):
    # find the first integer n >= x with bits matching pattern ...101010
    n = 0
    while n < x:
        n = (n << 2) | 0b10
    return n

print('1.', ceil_pattern(x) - x)
