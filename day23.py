from utils import get_input
from math import factorial
from day12 import VM

class VM2(VM):
    def tgl(self, x):
        n = self.read(x)
        if 0 <= self.ip + n < len(self.code):
            op = self.code[self.ip + n]
            match op[0]:
                case 'inc':
                    op[0] = 'dec'
                case 'dec' | 'tgl':
                    op[0] = 'inc'
                case 'jnz':
                    op[0] = 'cpy'
                case 'cpy':
                    op[0] = 'jnz'
        self.ip += 1

code = VM.parse(get_input(23))
c = int(code[19][1])
d = int(code[20][1])
print('1.', factorial(7) + c*d)
print('2.', factorial(12) + c*d)
