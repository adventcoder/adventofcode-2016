from utils import get_input

data = [int(c) for c in get_input(16).strip()]

def dragon_bit(i):
    '''Bit i of the dragon curve.'''
    #
    # From the recurrence:
    #
    # a(4 n)   = 0
    # a(4 n+2) = 1
    # a(2 n+1) = a(n)
    #
    #      i = (4 k+3) 2^n-1
    # bin(i) = xxxxx10(1)^n
    i += 1
    i //= (i & (-i))
    return int((i & 3) == 3)

def dragon_bit_count(n):
    '''sum(dragon_bit(i) for i in range(n))'''
    # https://oeis.org/A255070
    g = n ^ (n >> 1)
    return (n - g.bit_count()) >> 1

def checksum(size):
    block_size = size & (-size)
    n = size // block_size
    bits = []
    prev_parity = 0
    for i in range(n):
        parity = data_parity((i + 1) * block_size)
        prev_parity, block_parity = parity, parity ^ prev_parity
        bits.append(block_parity ^ 1) # we want XNOR (1 same, 0 different) so negate the parity
    return ''.join(str(bit) for bit in bits)

def data_parity(size):
    # The pattern of the data is: aDbDaDbD...
    #
    # Where:
    # - a is the data bits
    # - b is the data bits reversed and flipped
    # - D are the joiner bits (from the dragon curve)
    #
    pattern_size = len(data) + 1
    n = size // pattern_size
    r = size % pattern_size

    parity = 0
   
    # joiner bits
    parity ^= dragon_bit_count(n) & 1

    # full data chunks
    if n % 4 == 1: # a
        parity ^= sum(data) & 1
    elif n % 4 == 2: # ab
        parity ^= len(data) & 1
    elif n % 4 == 3: # aba
        parity ^= (len(data) - sum(data)) & 1 

    # remaining data chunk
    if n % 2 == 0:
        parity ^= sum(data[:r]) & 1
    else:
        parity ^= (r - sum(data[-r:])) & 1

    return parity

print('1.', checksum(272))
print('2.', checksum(35651584))
