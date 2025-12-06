from math import prod

with open("input.txt") as file:
    data = file.read().splitlines()

max_len = max(map(len, data))

for i in range(len(data)):
    if len(data[i]) < max_len:
        data[i] += ' ' * (max_len - len(data[i]))

elements = []
for x in range(len(data[0]) - 1, -1, -1):
    element = ''
    for y, line in enumerate(data):
        if y == len(data) - 1:
            elements.append(element)
            if element != ' ':
                elements.append(line[x])
        if line[x] != ' ':
            element += line[x]

result = 0

current_operation = []
for element in elements:
    if element in ['', ' ']:
        continue
    elif element == '+':
        if current_operation:
            result += sum(current_operation)
            current_operation = []
    elif element == '*':
        if current_operation:
            result += prod(current_operation)
            current_operation = []
    else:
        current_operation.append(int(element))

print(result)




# clean_data = []
# for line in data:
#     clean_data.append(list(filter(lambda x: x != '', line)))
#
# operations = {}
#
# for i in range(len(clean_data[0])):
#     operations[i] = []
#
# print(clean_data)
#
# for line in clean_data:
#     for key, element in enumerate(line):
#         operations[key].append(element)
#
# print(operations)
#
# result = 0
#
# for operation in operations.values():
#     action = operation.pop(-1)
#     operation = [int(x) for x in operation]
#     operation_parts = []
#     get_1 = lambda x: x % 10
#     get_10 = lambda x: (x // 10) % 10
#     get_100 = lambda x: (x // 100) % 10
#
#     for function in [get_100, get_10, get_1]:
#         new_part = ''
#         for part in operation:
#             digit = function(part)
#             if digit == 0:
#                 continue
#             new_part += str(function(part))
#         operation_parts.append(int(new_part))
#     print(operation_parts)
#
#
#
#
#     if action == '*':
#         result += prod(operation)
#     elif action == '+':
#         result += sum(operation)
#
#
# print(result)
