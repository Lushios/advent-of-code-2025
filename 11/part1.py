with open("input.txt") as file:
    data = file.read().splitlines()

connections = {}

for line in data:
    server_from, servers_to_str = line.split(": ")
    connections[server_from] = servers_to_str.split(' ')

print(connections)

paths = [['you']]

while True:
    new_paths = []
    for path in paths:
        last_server = path[-1]
        if last_server == 'out':
            new_paths.append(path)
            continue
        for connected_server in connections[last_server]:
            new_path = path + [connected_server]
            new_paths.append(new_path)
    paths = new_paths
    if all(path[-1] == 'out' for path in paths):
        break

print(paths)
print(len(paths))

