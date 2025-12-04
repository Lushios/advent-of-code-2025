with open("input.txt") as file:
    data = file.read().splitlines()

counter = 0
rolls_removed = []
started = False

def get_point_neighbors(x, y, field):
    neighbors = []
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),          (1, 0),
                  (-1, 1),  (0, 1),  (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(field[0]) and 0 <= ny < len(field):
            neighbors.append(field[ny][nx])
    return neighbors


while True:
    started = True
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ".":
                continue
            neighbors = get_point_neighbors(x, y, data)
            papers = [n for n in neighbors if n == '@']
            if len(papers) < 4:
                rolls_removed.append((x, y))
    print(data)
    print(len(rolls_removed))
    if len(rolls_removed) == 0:
        break
    for roll in rolls_removed:
        x, y = roll
        data[y] = data[y][:x] + "." + data[y][x+1:]
        counter += 1
    rolls_removed = []



print(counter)
