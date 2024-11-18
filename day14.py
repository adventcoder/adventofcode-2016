from utils import get_input
import hashlib
from collections import deque
from itertools import count, islice
import re

salt = get_input(14).strip()

def hash(i, reps):
    s = salt + str(i)
    for _ in range(reps + 1):
        s = hashlib.md5(s.encode('ascii')).hexdigest()
    return s

def key(hash, window):
    if m := re.search(r'(.)\1\1', hash):
        c = m.group(1)
        if any(c*5 in next for next in window):
            return True
    return False

def key_indexes(reps):
    window = deque()
    while len(window) < 1000:
        window.append(hash(len(window), reps))
    for i in count():
        window.append(hash(len(window) + i, reps))
        h = window.popleft()
        if key(h, window):
            yield i

def get(it, i):
    return next(islice(it, i, None))

print('1.', get(key_indexes(0), 63))
print('2.', get(key_indexes(2016), 63))
