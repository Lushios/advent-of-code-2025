from itertools import combinations
from functools import cache
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


with open("input.txt") as file:
    data = file.read().splitlines()

points = [(int(x), int(y)) for x, y in (line.split(',') for line in data)]

path = Path(points, closed=True) # 48494, 50273


# fig, ax = plt.subplots()
# patch = patches.PathPatch(path, facecolor='orange', lw=2)
# ax.add_patch(patch)
# # ax.set_xlim(0, 100000)
# ax.set_xlim(0, 15)
# # ax.set_ylim(0, 100000)
# ax.set_ylim(0, 15)
# plt.show()

rectangle_areas = {}

all_combos = list(combinations(points, 2)) # 122760
valid_combos = []

full_path = []
# horizontal_edges = []
# vertical_edges = []

def filter_combo_by_eye(combo, path):
    (x1, y1), (x2, y2) = combo
    # smaller_x, larger_x = min(x1, x2), max(x1, x2)
    smaller_y, larger_y = min(y1, y2), max(y1, y2)
    if smaller_y < 48400 and larger_y > 50400: #63228
        return False
    elif abs(x1 - x2) < 500 or abs(y1 - y2) < 500: # 60949
        return False
    else:
        return True


for i in range(len(points) - 1):
    if points[i][0] != points[i + 1][0]:
        diff = points[i + 1][0] - points[i][0]
        if diff > 0:
            for j in range(diff):
                full_path.append((points[i][0] + j, points[i][1]))
                # horizontal_edges.append((points[i][0] + j, points[i][1]))
            # horizontal_edges.pop()
        else:
            for j in range(0, diff, -1):
                full_path.append((points[i][0] + j, points[i][1]))
                # if j != 0:
                    # horizontal_edges.append((points[i][0] + j, points[i][1]))
    elif points[i][1] != points[i + 1][1]:
        diff = points[i + 1][1] - points[i][1]
        if diff > 0:
            for j in range(diff):
                full_path.append((points[i][0], points[i][1] + j))
                # vertical_edges.append((points[i][0], points[i][1] + j))
            # vertical_edges.pop()
        else:
            for j in range(0, diff, -1):
                full_path.append((points[i][0], points[i][1] + j))
                # if j != 0:
                    # vertical_edges.append((points[i][0], points[i][1] + j))

full_path = tuple(full_path)

combos = [combo for combo in all_combos if filter_combo_by_eye(combo, full_path)]
# combos = [((5398, 67501), (94737, 50273))]
a = len(combos)

def squash_intersections(intersections):
    squashed_intersections = []
    for key, inter in enumerate(intersections):
        if key == 0:
            squashed_intersections.append(inter)
        else:
            if abs(inter - squashed_intersections[-1]) != 1:
                squashed_intersections.append(inter)
            else:
                squashed_intersections.pop()
                squashed_intersections.append(inter)
    return squashed_intersections


def check_if_point_in_polygon_v3(point, polygon):
    if point in polygon:
        return True
    left_intersections = [p for p in polygon if p[1] == point[1] and p[0] < point[0]]
    right_intersections = [p for p in polygon if p[1] == point[1] and p[0] > point[0]]
    up_intersections = [p for p in polygon if p[0] == point[0] and p[1] > point[1]]
    down_intersections = [p for p in polygon if p[0] == point[0] and p[1] < point[1]]

    if not left_intersections or not right_intersections or not up_intersections or not down_intersections:
        return False
    return True


for key, combo in enumerate(combos):
    print(f"{key + 1} of {a}")
    (x1, y1), (x2, y2) = combo
    smaller_x, larger_x = min(x1, x2), max(x1, x2)
    smaller_y, larger_y = min(y1, y2), max(y1, y2)
    is_valid = True
    extremes = [(smaller_x, smaller_y), (smaller_x, larger_y), (larger_x, larger_y), (larger_x, smaller_y)]
    for extreme in extremes:
        if not check_if_point_in_polygon_v3(extreme, full_path):
            is_valid = False
            break
    if not is_valid:
        continue
    sides = [
        {'side': [(smaller_x, smaller_y), (smaller_x, larger_y)], 'direction': (0, 1), 'word': 'up'},
        {'side': [(smaller_x, larger_y), (larger_x, larger_y)], 'direction': (1, 0), 'word': 'right'},
        {'side': [(larger_x, larger_y), (larger_x, smaller_y)], 'direction': (0, -1), 'word': 'down'},
        {'side': [(larger_x, smaller_y), (smaller_x, smaller_y)], 'direction': (-1, 0), 'word': 'left'}
    ]
    for side in sides:
        if side['word'] == 'up':
            intersections_with_path_ys = [p[1] for p in full_path if p[0] == smaller_x and smaller_y <= p[1] <= larger_y and p not in extremes]
            if len(intersections_with_path_ys) > 0:
                intersections_ys = squash_intersections(intersections_with_path_ys)
                intersections_ys.insert(0, smaller_y)
                for i in range(len(intersections_ys) - 1):
                    if intersections_ys[i + 1] > intersections_ys[i]:
                        point = (smaller_x, intersections_ys[i] + 1)
                    else:
                        point = (smaller_x, intersections_ys[i] - 1)
                    point_valid = check_if_point_in_polygon_v3(point, full_path)
                    if not point_valid:
                        is_valid = False
                        break
        if side['word'] == 'right':
            intersections_with_path_xs = [p[0] for p in full_path if p[1] == larger_y and smaller_x <= p[0] <= larger_x and p not in extremes]
            if len(intersections_with_path_xs) > 0:
                intersections_xs = squash_intersections(intersections_with_path_xs)
                intersections_xs.insert(0, smaller_x)
                for i in range(len(intersections_xs) - 1):
                    if intersections_xs[i + 1] > intersections_xs[i]:
                        point = (intersections_xs[i] + 1, larger_y)
                    else:
                        point = (intersections_xs[i] - 1, larger_y)
                    point_valid = check_if_point_in_polygon_v3(point, full_path)
                    if not point_valid:
                        is_valid = False
                        break
        if side['word'] == 'down':
            intersections_with_path_ys = [p[1] for p in full_path if p[0] == larger_x and smaller_y <= p[1] <= larger_y and p not in extremes]
            if len(intersections_with_path_ys) > 0:
                intersections_ys = squash_intersections(intersections_with_path_ys)
                intersections_ys.insert(0, larger_y)
                for i in range(len(intersections_ys) - 1):
                    if intersections_ys[i + 1] > intersections_ys[i]:
                        point = (larger_x, intersections_ys[i] + 1)
                    else:
                        point = (larger_x, intersections_ys[i] - 1)
                    point_valid = check_if_point_in_polygon_v3(point, full_path)
                    if not point_valid:
                        is_valid = False
                        break
        if side['word'] == 'left':
            intersections_with_path_xs = [p[0] for p in full_path if p[1] == smaller_y and smaller_x <= p[0] <= larger_x and p not in extremes]
            if len(intersections_with_path_xs) > 0:
                intersections_xs = squash_intersections(intersections_with_path_xs)
                intersections_xs.insert(0, larger_x)
                for i in range(len(intersections_xs) - 1):
                    if intersections_xs[i + 1] > intersections_xs[i]:
                        point = (intersections_xs[i] + 1, smaller_y)
                    else:
                        point = (intersections_xs[i] - 1, smaller_y)
                    point_valid = check_if_point_in_polygon_v3(point, full_path)
                    if not point_valid:
                        is_valid = False
                        break

        if not is_valid:
            print('invalid', side)
            break

    if is_valid:
        valid_combos.append(combo)

max_area = 0
max_combo = ()
for combo in valid_combos:
    rectangle_areas[combo] = (abs(combo[0][0] - combo[1][0]) + 1) * (abs(combo[0][1] - combo[1][1]) + 1)
    if rectangle_areas[combo] >= max_area:
        max_area = rectangle_areas[combo]
        max_combo = combo

print(max_area)
print(max_combo)






def check_if_point_in_polygon_v2(point, vertical_edges):
    if point in full_path:
        return True
    x, y = point
    intersections_to_the_right_xs = [p[0] for p in vertical_edges if p[1] == y and p[0] > x]
    # squashed_intersections = squash_intersections(intersections_to_the_right_xs)
    if len(intersections_to_the_right_xs) % 2 == 1:
        return True
    else:
        return False


@cache
def check_if_point_in_polygon(point, polygon):
    if point in polygon:
        return True
    x, y = point
    intersections_to_the_right_xs = [p[0] for p in polygon if p[1] == y and p[0] > x]
    squashed_intersections = squash_intersections(intersections_to_the_right_xs)
    if len(squashed_intersections) % 2 == 1:
        return True
    else:
        intersections_to_the_left_xs = [p[0] for p in polygon if p[1] == y and p[0] < x]
        squashed_intersections = squash_intersections(intersections_to_the_left_xs)
        if len(squashed_intersections) % 2 == 1:
            return True
        else:
            intersections_up_ys = [p[1] for p in polygon if p[0] == x and p[1] > y]
            squashed_intersections = squash_intersections(intersections_up_ys)
            if len(squashed_intersections) % 2 == 1:
                return True
            else:
                intersections_down_ys = [p[1] for p in polygon if p[0] == x and p[1] < y]
                squashed_intersections = squash_intersections(intersections_down_ys)
                if len(squashed_intersections) % 2 == 1:
                    return True
                else:
                    return False