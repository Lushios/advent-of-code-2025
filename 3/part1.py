with open("input.txt") as file:
    data = file.read().splitlines()


result = 0

for line in data:
    battery1index = None
    battery2index = None
    for i in range(9, 0, -1):
        temp = line.find(str(i))
        if temp == len(line) - 1 or temp == -1:
            continue
        battery1index = temp
        break
    for i in range(9, 0, -1):
        temp = line.find(str(i), battery1index + 1)
        if temp == -1:
            continue
        battery2index = temp
        break

    batteries = line[battery1index] + line[battery2index]
    result += int(batteries)

print(result)


