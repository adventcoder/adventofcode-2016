from utils import get_input
from math import log, floor

def winner1(n):
    # Even case:
    # ---------
    # v         v
    # 012345 -> 0x2x4x
    #
    # winner(2 n) = 2 winner(n)
    #
    # Odd case:
    # --------
    # v            v
    # 0123456 -> xx2x4x6
    #
    # winner(2 n+1) = 2 winner(n) + 2
    #
    # Solve:
    # -----
    #
    # winner(2^n + a) = 2 a, 0<=a<2^n
    #
    msb = 1 << (n.bit_length() - 1)
    return (n ^ msb) << 1

def winner2(n):
    # winner(  3^n + a + 1) = a, 0<=a<3^n
    # winner(2 3^n + a + 1) = 2 a, 0<=a<3^n
    if n == 1:
        return 0
    n -= 1
    p = 3**floor(log(n, 3))
    d, a = divmod(n, p)
    return d * a

n = int(get_input(19))
print('1.', winner1(n) + 1)
print('2.', winner2(n) + 1)
