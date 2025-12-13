from random import randint

with open("input2.txt") as file:
    data = file.read().splitlines()

connections = {}
inverted_connections = {}

for line in data:
    server_from, servers_to_str = line.split(": ")
    servers_to = servers_to_str.split(' ')
    connections[server_from] = servers_to
    for server_to in servers_to:
        if server_to in inverted_connections:
            inverted_connections[server_to].append(server_from)
        else:
            inverted_connections[server_to] = [server_from]


seth = set()
helper = {}
def search_the_paths(current, destination, all_paths, path, graph, banned_nodes, counter):
    if current != destination and current in seth:
        # helper[path[-1]] = helper[current] * 2
        path.append(current)
        counter += helper[path - 1]
        # all_paths.append(path.copy())
        return counter

    if current in banned_nodes:
        return counter

    path.append(current)
    if current == destination:
        # helper[path[-2]] = 1
        for node in path:
            seth.add(node)
        counter += 1
        # all_paths.append(path.copy()) 1  2 -
    else:
        for connection in graph.get(current, []):
            if connection not in path:
                # тут можна порахувати скільки повернулось сумарно, і якщо більше 1, записати в словник
                counter = search_the_paths(connection, destination, all_paths, path, graph, banned_nodes, counter)
            else:
                return counter
    path.pop()
    return counter



def get_paths(source, destination, graph, banned_nodes=[]):
    all_paths = []
    path = []
    counter = 0
    search_the_paths(source, destination, all_paths, path, graph, banned_nodes, counter)

    return all_paths


result = get_paths('svr', 'out', connections, [])

for line in result:
    print(line)
print(len(result))
