import hashlib
from utils import get_input

door_id = get_input(5)

def gethash(n):
    return hashlib.md5(bytes(door_id + str(n), 'ascii')).hexdigest()

password1 = []
password2 = [None] * 8
found = 0
n = 0
while found < len(password2):
    hash = gethash(n)
    n += 1
    if hash.startswith('00000'):
        if len(password1) < 8:
            password1.append(hash[5])
        i = int(hash[5], 16)
        if i < len(password2) and password2[i] is None:
            password2[i] = hash[6]
            found += 1

print('1.', ''.join(password1))
print('2.', ''.join(password2))
