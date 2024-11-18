
class Font:
    @classmethod
    def read(cls, filename, *args, **kwargs):
        with open(filename, 'r') as file:
            return cls.parse(file.read(), *args, **kwargs)

    @classmethod
    def parse(cls, s):
        chars, chunk = s.split('\n\n')
        grid = chunk.splitlines()
        grid_width = max(map(len, grid))
        font = cls(grid_width // len(chars), len(grid))
        font.store(chars, grid)
        return font

    def __init__(self, glyph_width, glyph_height):
        self.glyph_width = glyph_width
        self.glyph_height = glyph_height
        self.chars = {}

    def store(self, chars, grid, offset_x=0, offset_y=0):
        x = offset_x
        for c in chars:
            self.chars[self.glyph_key(grid, x, offset_y)] = c
            x += self.glyph_width

    def lookup(self, grid, x, y):
        key = self.glyph_key(grid, x, y)
        try:
            return self.chars[key]
        except KeyError:
            return ' ' if key == 0 else '?'

    def glyph_key(self, grid, offset_x, offset_y):
        n = 0
        for y in range(self.glyph_height):
            for x in range(self.glyph_width):
                n = (n << 1) | int(getpixel(grid, x + offset_x, y + offset_y))
        return n

def getpixel(grid, x, y):
    try:
        return grid[y][x] == '#'
    except IndexError:
        return False

letters5x6 = Font.read('fonts/letters5x6.txt')
