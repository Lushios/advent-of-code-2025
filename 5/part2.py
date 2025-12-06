from copy import deepcopy

with open("input.txt") as file:
    data = file.read()


fresh_str, _ = data.split('\n\n')

fresh = fresh_str.splitlines()

ranges = []

for line in fresh:
    part1, part2 = line.split('-')
    ranges.append((int(part1), int(part2)))

while True:
    old_len = len(ranges)
    for range in ranges:
        for other_range in ranges:
            if range == other_range:
                continue
            if range[0] <= other_range[0] <= range[1] or range[0] <= other_range[1] <= range[1]:
                new_start = min(range[0], other_range[0])
                new_end = max(range[1], other_range[1])
                ranges.remove(range)
                ranges.remove(other_range)
                ranges.append((new_start, new_end))
                break

    print(len(ranges))
    if old_len == len(ranges):
        break

ranges = set(ranges)

sum = 0
for range in ranges:
    sum += range[1] - range[0] + 1

print(sum)



