from utils import get_input
from collections import Counter

rows = get_input(6).splitlines()

msg1 = []
msg2 = []
for col in zip(*rows):
    counts = Counter(col)
    msg1.append(max(counts, key=counts.get))
    msg2.append(min(counts, key=counts.get))

print('1.', ''.join(msg1))
print('2.', ''.join(msg2))
