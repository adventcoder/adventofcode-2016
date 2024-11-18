from utils import get_input

ranges = []
for line in get_input(20).splitlines():
    a, b = line.split('-')
    ranges.append(range(int(a), int(b) + 1))

result = [range(0, 0)]
ranges.sort(key=lambda rng: rng.start)
for rng in ranges:
    if rng.start <= result[-1].stop:
        result[-1] = range(result[-1].start, max(rng.stop, result[-1].stop))
    else:
        result.append(rng)

print('1.', result[0].stop)
print('2.', 4294967296 - sum(len(rng) for rng in result))
