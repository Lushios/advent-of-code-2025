from copy import deepcopy
from itertools import product, permutations, repeat, combinations
from functools import cache

with open("input.txt") as file:
    data = file.read().splitlines()

@cache
def press_button(input, button):
    input = list(input)
    for value in button:
        input[value] = not input[value]
    return tuple(input)


@cache
def solve_for_combo(input_length, combo):
    last_button = combo[-1]
    if len(combo) > 1:
        solution_without_last = solve_for_combo(input_length, combo[:-1])
    else:
        solution_without_last = tuple([False] * input_length)
    return press_button(solution_without_last, last_button)



answer = 0

for key, line in enumerate(data):
    print('line ', key + 1 , 'of', len(data))
    first_cut = line.find(' ')
    first_block = line[:first_cut]
    second_cut = line.find('{') - 1
    second_block = line[first_cut + 1 : second_cut]
    third_block = line[second_cut + 1 :]
    indicators_str = first_block[1:-1]
    indicators = []
    for ind in indicators_str:
        if ind == '.':
            indicators.append(False)
        else:
            indicators.append(True)
    indicators = tuple(indicators)
    buttons = []
    for btn in second_block.split(' '):
        ids = btn.replace('(', '').replace(')', '').split(',')
        button = tuple(int(id_) for id_ in ids)
        buttons.append(button)
    for i in range(1, 1000):
        print(i)
        solution = None
        combos = combinations(buttons, i)
        for combo in combos:
            state = solve_for_combo(len(indicators), combo)
            if state == indicators:
                solution = len(combo)
                break
        if solution is not None:
            answer += solution
            break


print(answer)


