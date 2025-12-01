with open("input.txt") as file:
    data = file.read().splitlines()

value = 50
counter = 0

for instruction in data:
    operation, number = instruction[0], int(instruction[1:])

    if operation == 'R':
        value += number
    elif operation == 'L':
        value -= number

    value = value % 100

    if value == 0:
        counter += 1


print(counter)