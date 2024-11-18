from utils import get_input, sgn
import re

#
# We have:
#
# a = a1 mod m1
# a = a2 mod m2
#
# From bezout find n1, n2 such that:
#
# n1 m1 + n2 m2 = gcd(m1, m2)
#
# Now define:
#
# a gcd(m1,m2) = a1 n2 m2 + a2 n1 m1, with a1 = a2 mod gcd(m1,m2)
#
# We can check it satisfies the original system:
#
# a gcd(m1,m2) = a2 n1 m1 mod m2
#              = a2 (gcd(m1,m2) - n2 m2) mod m2
#            a = a2 mod m2
#
# a gcd(m1,m2) = a1 n2 m2 mod m1
#              = a1 (gcd(m1,m2) - n1 m1) mod m1
#            a = a1 mod m1
#
def crt(eqn1, eqn2):
    a1, m1 = eqn1
    a2, m2 = eqn2
    d, n1, n2 = bezout(m1, m2)
    assert a1 % d == a2 % d
    a = (a1*n2*m2 + a2*n1*m1) // d
    m = (m1*m2) // d
    return a % m, m

def bezout(a, b):
    d1, n1, m1 = abs(a), sgn(a), 0
    d2, n2, m2 = abs(b), 0, sgn(b)
    while d2 != 0:
        q = d1 // d2
        d1, d2 = d2, d1 - q*d2
        n1, n2 = n2, n1 - q*n2
        m1, m2 = m2, m1 - q*m2
    return d1, n1, m1

times = (0, 1)
depth = 1
for line in get_input(15).splitlines():
    tokens = re.sub(r'[;,.]', '', line).split()
    size = int(tokens[3])
    start = int(tokens[-1])
    times = crt(times, (-start - depth, size))
    depth += 1
print('1.', times[0])

times = crt(times, (-depth, 11))
print('2.', times[0])
