from utils import get_input
import re

def abba(seq):
    for i in range(len(seq) - 3):
        a, b, c, d = seq[i:i+4]
        if a == d and b == c and a != b:
            return True
    return False

def aba(seqs):
    for seq in seqs:
        for i in range(len(seq) - 2):
            a, b, c = seq[i:i+3]
            if a == c and a != b:
                yield a + b + a

def bab(seqs):
    for seq in seqs:
        for i in range(len(seq) - 2):
            a, b, c = seq[i:i+3]
            if a == c and a != b:
                yield b + a + b

tls = 0
ssl = 0
for seq in get_input(7).splitlines():
    supernet = re.split(r'\[[^]]*\]', seq)
    hypernet = re.findall(r'\[([^]]*)\]', seq)
    tls += any(map(abba, supernet)) and not any(map(abba, hypernet))
    ssl += bool(set(bab(supernet)) & set(aba(hypernet)))

print('1.', tls)
print('2.', ssl)
