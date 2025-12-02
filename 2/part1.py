with open("input.txt") as file:
    data = file.read().splitlines()[0]

data = data.split(',')

counter = 0

for instruction in data:
    first_encounter = None
    number1, number2 = instruction.split('-')
    len1, len2 = len(number1), len(number2)
    number1, number2 = int(number1), int(number2)
    for i in range(number1, number2 + 1):
        i = str(i)
        if i[:len(i)//2] == i[len(i)//2:]:
            first_encounter = int(i)
            break

    if first_encounter is not None:
        if len2 == 2 or len1 == 2:
            for i in range(first_encounter, number2 + 1, 11):
                if len(str(i)) == 2:
                    counter += i
        elif len2 == 4 or len1 == 4:
            for i in range(first_encounter, number2 + 1, 101):
                if len(str(i)) == 4:
                    counter += i
        elif len2 == 6 or len1 == 6:
            for i in range(first_encounter, number2 + 1, 1001):
                if len(str(i)) == 6:
                    counter += i
        elif len2 == 8 or len1 == 8:
            for i in range(first_encounter, number2 + 1, 10001):
                if len(str(i)) == 8:
                    counter += i
        elif len2 == 10 or len1 == 10:
            for i in range(first_encounter, number2 + 1, 100001):
                if len(str(i)) == 10:
                    counter += i

print(counter)
