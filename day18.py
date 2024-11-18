from utils import get_input

# abc   a^c
# ... -> .
# ..^ -> ^
# .^. -> .
# .^^ -> ^
# ^.. -> ^
# ^.^ -> .
# ^^. -> ^
# ^^^ -> .

def parse(s):
    traps = 0
    for c in s:
        traps = (traps << 1) | '.^'.index(c)
    all = (1 << len(s)) - 1
    return traps, all

def step(traps, all):
    return ((traps << 1) ^ (traps >> 1)) & all

traps, all = parse(get_input(18).strip())
safe = (traps ^ all).bit_count()

for _ in range(40 - 1):
    traps = step(traps, all)
    safe += (traps ^ all).bit_count()
print('1.', safe)

for _ in range(400000 - 40):
    traps = step(traps, all)
    safe += (traps ^ all).bit_count()
print('2.', safe)
