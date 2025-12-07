from functools import cache

def cache_notify(func):
    func = cache(func)
    def notify_wrapper(*args, **kwargs):
        stats = func.cache_info()
        hits = stats.hits
        results = func(*args, **kwargs)
        stats = func.cache_info()
        if stats.hits > hits:
            print(f"NOTE: {func.__name__}({args}) results were cached")
        return results
    return notify_wrapper

with open("input.txt") as file:
    data = file.read().splitlines()

start = data[0].find('S')



adjacency_list = {}

def fill_adjacency_list_for_point(x, y):
    if (x, y) in adjacency_list:
        return
    if y == len(data) - 1:
        adjacency_list[(x, y)] = None
        return
    neighbors = []
    for new_y in range(y + 1, len(data)):
        if data[new_y][x] == '.':
            continue
        elif data[new_y][x] == '^':
            neighbors.append((x - 1, new_y))
            neighbors.append((x + 1, new_y))
            break
    adjacency_list[(x, y)] = neighbors
    for neighbor in neighbors:
        fill_adjacency_list_for_point(neighbor[0], neighbor[1])

fill_adjacency_list_for_point(start, 0)

print(adjacency_list)

counter = 0


@cache_notify
def get_number_of_paths_from_point(point):
    neighbors = adjacency_list[point]
    total_paths = 0
    for neighbor in neighbors:
        if not adjacency_list[neighbor]:
            total_paths += 1
        else:
            total_paths += get_number_of_paths_from_point(neighbor)
    return total_paths



a = get_number_of_paths_from_point((start, 0))

print(a)





#
# @cache_notify
# def get_all_possible_paths(x,  y):
#     print(x, y)
#     if y == len(data) - 1:
#         return [(x, y)]
#     all_paths = set()
#     for new_y in range(y+1, len(data) - 1):
#         if data[new_y][x] == '.':
#             continue
#         elif data[new_y][x] == '^':
#             left_paths = get_all_possible_paths(x - 1, new_y)
#             right_paths = get_all_possible_paths(x + 1, new_y)
#             for path in left_paths:
#                 new_path = ((x, y), (path[0], path[1]))
#                 all_paths.add(new_path)
#             for path in right_paths:
#                 new_path = ((x, y), (path[0], path[1]))
#                 all_paths.add(new_path)
#         return all_paths
#     return [(x, y)]
#
#
# a = get_all_possible_paths(start, 0)
#
# for i in a:
#     print(i)
#
# print(len(a))





# splitters = {}
#
# for i in range(len(data)):
#     line_splitters = [key for key, value in enumerate(data[i]) if value == '^']
#     if line_splitters:
#         splitters[i] = line_splitters
#
# beams = [start]
# nodes = {0: {start}}
#
# for y in range (1, len(data)):
#     new_beams = set(beams)
#     for x in beams:
#         if data[y][x] == '.':
#             continue
#         if data[y][x] == '^':
#             if y in nodes:
#                 nodes[y].extend([x - 1, x + 1])
#             else:
#                 nodes[y] = [x - 1, x + 1]
#             new_beams.remove(x)
#             new_beams.add(x - 1)
#             new_beams.add(x + 1)
#     if y in nodes:
#         nodes[y] = set(nodes[y])
#     beams = set(new_beams)
#
# new_nodes = []
#
# for key, value in nodes.items():
#     new_nodes.append(list(value))
#
# print(new_nodes)
# print(nodes)
#
#
# def find_possible_paths(level, starting_point, nodes):
#     if level + 2 not in nodes:
#         return [starting_point]
#     possible_next_points = list(filter(lambda x: abs(x - starting_point) == 1, nodes[level + 2]))
#     possible_routes = []
#     for possible_next_point in possible_next_points:
#         new_possible_paths = find_possible_paths(level + 2, possible_next_point, nodes)
#         route = [starting_point] + new_possible_paths
#         possible_routes.append(route)
#     return possible_routes
#
#
# a = find_possible_paths(12, 11, nodes)
# print(a)

