with open("input.txt") as file:
    data = file.read().splitlines()


result = 0


def find_largest_number_in_range(line, start, end):
    largest = -1
    index = 0
    for current_index, battery in enumerate(line):
        if current_index < start:
            continue
        elif current_index > end:
            break

        if int(battery) > largest:
            largest = int(battery)
            index = current_index

    return largest, index

for line in data:
    battery_bank = ''
    current_index = -1
    for i in range(1, 13):
        largest, index = find_largest_number_in_range(line, current_index + 1, len(line) - 12 + len(battery_bank))
        current_index = index
        battery_bank += str(largest)
    result += int(battery_bank)




    # new_battery = line
    # for i in range (1, 10):
    #     i = str(i)
    #     while i in new_battery:
    #         new_battery = new_battery.replace(i, '', 1)
    #         if len(new_battery) == 12:
    #             break
    #     if len(new_battery) == 12:
    #         break
    # result += int(new_battery)

print(result)


