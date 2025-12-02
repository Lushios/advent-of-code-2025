import re

with open("input.txt") as file:
    data = file.read().splitlines()[0]

data = data.split(',')

counter = 0


for instruction in data:
    number1, number2 = instruction.split('-')
    len1, len2 = len(number1), len(number2)
    number1, number2 = int(number1), int(number2)

    # when I wrote this, I realised I could leverage the dividers of the len number, but whatever, I have a reservation at the restaurant to make it to
    for i in range(number1, number2 + 1):
        i = str(i)
        if len(i) == 2:
            if i[0] == i[1]:
                counter += int(i)
        elif len(i) == 3:
            if i[0] == i[1] == i[2]:
                counter += int(i)
        elif len(i) == 4:
            if (i[0] == i[1] == i[2] == i[3]) or (i[:2] == i[2:]):
                counter += int(i)
        elif len(i) == 5:
            if i[0] == i[1] == i[2] == i[3] == i[4]:
                counter += int(i)
        elif len(i) == 6:
            if (i[0] == i[1] == i[2] == i[3] == i[4] == i[5]) or (i[:3] == i[3:]) or (i[:2] == i[2:4] == i[4:]):
                counter += int(i)
        elif len(i) == 7:
            if i[0] == i[1] == i[2] == i[3] == i[4] == i[5] == i[6]:
                counter += int(i)
        elif len(i) == 8:
            if (i[0] == i[1] == i[2] == i[3] == i[4] == i[5] == i[6] == i[7]) or (i[:4] == i[4:]) or (i[:2] == i[2:4] == i[4:6] == i[6:]):
                counter += int(i)
        elif len(i) == 9:
            if (i[0] == i[1] == i[2] == i[3] == i[4] == i[5] == i[6] == i[7] == i[8]) or (i[:3] == i[3:6] == i[6:9]):
                counter += int(i)
        elif len(i) == 10:
            if (i[0] == i[1] == i[2] == i[3] == i[4] == i[5] == i[6] == i[7] == i[8] == i[9]) or (i[:5] == i[5:]) or (i[:2] == i[2:4] == i[4:6] == i[6:8] == i[8:]):
                counter += int(i)


print(counter)
