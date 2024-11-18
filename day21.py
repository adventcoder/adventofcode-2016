from utils import get_input, sgn

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def reverse(arr, i, j):
    while i < j:
        swap(arr, i, j)
        i += 1
        j -= 1

def rotate(arr, n):
    rotate_range(arr, n, 0, len(arr) - 1)

def rotate_range(arr, n, i, j):
    n %= (j - i + 1)
    reverse(arr, i, j)
    reverse(arr, i, i + n - 1)
    reverse(arr, i + n, j)

def parse_commands(input):
    commands = []
    for line in input.splitlines():
        match line.split():
            case ['swap', 'position', x, 'with', 'position', y]:
                commands.append(swap_command(int(x), int(y)))
            case ['swap', 'letter', x, 'with', 'letter', y]:
                commands.append(swap_letters_command(x, y))
            case ['rotate', 'right', x, ('step' | 'steps')]:
                commands.append(rotate_command(int(x)))
            case ['rotate', 'left', x, ('step' | 'steps')]:
                commands.append(rotate_command(-int(x)))
            case ['rotate', 'based', 'on', 'position', 'of', 'letter', x]:
                commands.append(rotate_based_command(x))
            case ['reverse', 'positions', x, 'through', y]:
                commands.append(reverse_command(int(x), int(y)))
            case ['move', 'position', x, 'to', 'position', y]:
                commands.append(move_command(int(x), int(y)))
    return commands

def swap_command(x, y):
    f = lambda pwd: swap(pwd, x, y)
    return f, f

def swap_letters_command(x, y):
    f = lambda pwd: swap(pwd, pwd.index(x), pwd.index(y))
    return f, f

def rotate_command(x):
    f = lambda pwd: rotate(pwd, x)
    f_inv = lambda pwd: rotate(pwd, -x)
    return f, f_inv

def rotate_range_command(x, i, j):
    f = lambda pwd: rotate_range(pwd, x, i, j)
    f_inv = lambda pwd: rotate_range(pwd, -x, i, j)
    return f, f_inv

def rotate_based_command(x):
    def f(pwd):
        i = pwd.index(x)
        j = (i + 1 + (i >= 4)) % len(pwd)
        rotate(pwd, j - i)
    def f_inv(pwd):
        j = pwd.index(x)
        i = [(2*i + 1 + (i >= 4)) % len(pwd) for i in range(len(pwd))].index(j)
        rotate(pwd, i - j)
    return f, f_inv

def reverse_command(i, j):
    f = lambda pwd: reverse(pwd, i, j)
    return f, f

def move_command(i, j):
    return rotate_range_command(sgn(i - j), min(i, j), max(i, j))

commands = parse_commands(get_input(21))

pwd = list('abcdefgh')
for f, _ in commands:
    f(pwd)
print('1.', ''.join(pwd))

pwd = list('fbgdceah')
for _, f_inv in reversed(commands):
    f_inv(pwd)
print('2.', ''.join(pwd))
