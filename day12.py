from utils import get_input

class VM:
    @classmethod
    def parse(cls, input):
        return [line.split() for line in input.splitlines()]

    def __init__(self, code):
        self.code = code
        self.mem = { c: 0 for c in 'abcd' }
        self.ip = 0

    def read(self, x):
        if x in self.mem:
            return self.mem[x]
        else:
            return int(x)

    def write(self, x, val):
        if x in self.mem:
            self.mem[x] = val

    def cpy(self, x, y):
        self.write(y, self.read(x))
        self.ip += 1

    def jnz(self, x, y):
        self.ip += self.read(y) if self.read(x) != 0 else 1

    def inc(self, x):
        self.write(x, self.read(x) + 1)
        self.ip += 1

    def dec(self, x):
        self.write(x, self.read(x) - 1)
        self.ip += 1

    def run(self):
        while 0 <= self.ip < len(self.code):
            if self.match_mul(self.ip):
                pass
            elif m := self.match_add(self.ip):
                x, y = m
                self.write(x, self.read(x) + self.read(y))
                self.write(y, 0)
                self.ip += 3
            else:
                op, *args = self.code[self.ip]
                getattr(self, op)(*args)

    def match_mul(self, ip):
        # inc x
        # dec y
        # jnz y -2
        # dec z
        # jnz z -5
        return None

    def match_add(self, ip):
        # inc x
        # dec y
        # jnz y -2
        if ip < len(self.code) - 2:
            a, b, c = self.code[self.ip : self.ip + 3]
            if a[0] == 'inc' and b[0] == 'dec' and b[1] != a[1] and c[0] == 'jnz' and c[1] == b[1] and c[2] == '-2':
                return a[1], b[1]
        return None

def exec(code, c):
    vm = VM(code)
    vm.write('c', c)
    vm.run()
    return vm.read('a')

code = VM.parse(get_input(12))
print('1.', exec(code, 0))
print('2.', exec(code, 1))
