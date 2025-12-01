with open("input.txt") as file:
    data = file.read().splitlines()

value = 50
counter = 0
number = 3

for instruction in data:
    original_number = number
    operation, number = instruction[0], int(instruction[1:])
    previous_value = value

    if operation == 'R':
        while value + number > 99:
            number -= 100
            counter += 1
        value += number
    elif operation == 'L':
        while value - number < 0:
            number -= 100
            counter += 1
        value -= number
        if previous_value == 0 and value != 0:
            counter -= 1

    if value == 0 and original_number < 100 and operation == 'L':
        counter += 1


    # prev_value = value

    # if operation == 'R':
    #     value += number
    # elif operation == 'L':
    #     value -= number

    # if value < 0 or value >= 100:
    #     counter += abs(value // 100)
    #
    # if value == 0:
    #     counter += 1
    #
    # # if prev_value == 0 and value < 0:
    # #     counter -= 1
    #
    # value = value % 100
    #
    # # if value == 0:
    # #     counter += 1
    #
    # print(instruction, value, counter)


print(counter)