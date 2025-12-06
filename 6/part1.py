from math import prod

with open("input.txt") as file:
    data = file.read().splitlines()



data = [list(line.split(' ')) for line in data]

clean_data = []
for line in data:
    clean_data.append(list(filter(lambda x: x != '', line)))

operations = {}

for i in range(len(clean_data[0])):
    operations[i] = []

for line in clean_data:
    for key, element in enumerate(line):
        operations[key].append(element)

result = 0

print(operations)

for operation in operations.values():
    action = operation.pop(-1)
    operation = [int(x) for x in operation]
    if action == '*':
        result += prod(operation)
    elif action == '+':
        result += sum(operation)


print(result)
