from itertools import combinations

with open("input.txt") as file:
    data = file.read().splitlines()

points = [(int(x), int(y)) for x, y in (line.split(',') for line in data)]

rectangle_areas = {}

combos = combinations(points, 2)

for combo in combos:
    print(combo)
    rectangle_areas[combo] = abs(combo[0][0] - combo[1][0] + 1) * abs(combo[0][1] - combo[1][1] + 1)

print(max(rectangle_areas.values()))
