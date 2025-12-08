from copy import deepcopy
from itertools import combinations
from math import sqrt

with open("input.txt") as file:
    data = file.read().splitlines()


def sort_two_boxes(box1, box2):
    return tuple(sorted([box1, box2], key=lambda b: (b[0], b[1], b[2])))

boxes_coords = []
coords_to_distances = {}

for line in data:
    x, y, z = line.split(',')
    boxes_coords.append((int(x), int(y), int(z)))

for i, box1 in enumerate(boxes_coords):
    for box2 in boxes_coords[i + 1:]:
        dx = box1[0] - box2[0]
        dy = box1[1] - box2[1]
        dz = box1[2] - box2[2]
        distance = sqrt(dx * dx + dy * dy + dz * dz)
        coords_to_distances[(sort_two_boxes(box1, box2))] = distance

distances_to_coords = {value: key for key, value in coords_to_distances.items()}

distances = sorted(distances_to_coords.keys())

connections = []

for i in range(1000):
    connections.append(distances_to_coords[distances[i]])

print(connections)

groups = deepcopy(boxes_coords)

print(groups)

def find_complex_group_box_belongs_to(box, grps):
    for index, grp in enumerate(grps):
        if type(grp) == tuple:
            continue
        if box in grp:
            return index
    return None


for point1, point2 in connections:
    print(point1, point2)
    if point1 in groups and point2 in groups:
        groups.remove(point1)
        groups.remove(point2)
        groups.append([point1, point2])
    elif point1 in groups and point2 not in groups:
        point2group = find_complex_group_box_belongs_to(point2, groups)
        groups[point2group].append(point1)
        groups.remove(point1)
    elif point2 in groups and point1 not in groups:
        point1group = find_complex_group_box_belongs_to(point1, groups)
        groups[point1group].append(point2)
        groups.remove(point2)
    elif point1 not in groups and point2 not in groups:
        point1group = find_complex_group_box_belongs_to(point1, groups)
        point2group = find_complex_group_box_belongs_to(point2, groups)
        if point1group == point2group:
            continue
        groups[point1group].extend(groups[point2group])
        del groups[point2group]

complex_groups = sorted(filter(lambda g: type(g) == list, groups), key=len, reverse=True)

print(len(complex_groups[0]) * len(complex_groups[1]) * len(complex_groups[2]))






# unique_distances = set(distances.values())
# print(len(distances), len(unique_distances))
