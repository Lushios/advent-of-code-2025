with open("input.txt") as file:
    data = file.read().splitlines()

start = data[0].find('S')

beams = [start]

splits = 0

for y in range (1, len(data)):
    new_beams = set(beams)
    for x in beams:
        if data[y][x] == '.':
            continue
        if data[y][x] == '^':
            splits += 1
            new_beams.remove(x)
            new_beams.add(x - 1)
            new_beams.add(x + 1)
    beams = set(new_beams)

# print(splits)
print(len(beams))
