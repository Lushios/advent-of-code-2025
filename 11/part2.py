from random import randint

with open("input.txt") as file:
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



def search_the_paths(current, destination, all_paths, helper, path, graph, banned_nodes, counter):
    if current in banned_nodes:
        return counter
    path.append(current)
    should_quit = False # maybe cut this var
    if current == destination:
        counter += 1
        # all_paths.append(path.copy())
    else:
        local_counter = 0
        for connection in graph.get(current, []):
            if connection not in path:
                prev_counter = counter
                if connection in helper:
                    # local_counter += helper[connection]
                    counter += helper[connection]
                else:
                    counter = search_the_paths(connection, destination, all_paths, helper, path, graph, banned_nodes, counter)
                local_counter += counter - prev_counter
            else:
                should_quit = True
        helper[current] = local_counter
    if not should_quit:
        path.pop()
    return counter




def get_paths(source, destination, graph, banned_nodes=[]):
    helper = {}
    path = []
    all_paths = []
    counter = 0
    result = search_the_paths(source, destination, all_paths, helper, path, graph, banned_nodes, counter)
    return result

    # return all_paths


# forbid going through dac in the beginning, do it separately
# source = 'svr'
# destination = 'dac'

# svr_to_out = get_paths('svr', 'out', connections, [])
# print(svr_to_out)


# svr_to_out = get_paths('svr', 'out', connections, [])
# print(svr_to_out)




svr_to_dac = get_paths('svr', 'dac', connections, ['fft', 'out'])
dac_to_fft = get_paths('dac', 'fft', connections, ['svr', 'out']) if svr_to_dac else 0
fft_to_out = get_paths('fft', 'out', connections, ['dac', 'svr']) if dac_to_fft else 0

svr_to_fft = get_paths('svr', 'fft', connections, ['dac', 'out'])
fft_to_dac = get_paths('fft', 'dac', connections, ['svr', 'out']) if svr_to_fft else 0
dac_to_out = get_paths('dac', 'out', connections, ['fft', 'svr']) if fft_to_dac else 0


print(f"svr_to_dac: {svr_to_dac}, dac_to_fft: {dac_to_fft}, fft_to_out: {fft_to_out}")
print(f"svr_to_fft: {svr_to_fft}, fft_to_dac: {fft_to_dac}, dac_to_out: {dac_to_out}")
result = (svr_to_dac * dac_to_fft * fft_to_out) + (svr_to_fft * fft_to_dac * dac_to_out)

print(result)


# dac_to_svr = get_paths('dac', 'svr', inverted_connections, ['fft', 'out'])
# print(len(dac_to_svr))
# fft_to_svr = get_paths('fft', 'svr', inverted_connections, ['dac', 'out'])
# print(len(fft_to_svr))
# fft_to_dac = get_paths('fft', 'dac', inverted_connections, ['svr', 'out'])
# print(len(fft_to_dac))
# dac_to_fft = get_paths('dac', 'fft', inverted_connections, ['svr', 'out'])
# print(len(dac_to_fft))
# out_to_dac = get_paths('out', 'dac', inverted_connections, ['fft', 'svr'])
# print(len(out_to_dac))
# out_to_fft = get_paths('out', 'fft', inverted_connections, ['dac', 'svr'])
# print(len(out_to_fft))
#
# fft_to_dac2 = get_paths('fft', 'dac', connections, ['svr', 'out'])
# print(len(fft_to_dac2))
# dac_to_fft2 = get_paths('dac', 'fft', connections, ['svr', 'out'])
# print(len(dac_to_fft2))

# fft_to_dac = get_paths('fft', 'dac', connections, ['out'])
# print(len(fft_to_dac))

# dac_to_fft = get_paths('dac', 'fft', connections, ['out', 'svr'])
# print(len(dac_to_fft))
#
# inverted_fft_to_dac = get_paths('dac', 'fft', inverted_connections, ['out', 'svr'])
# print(len(inverted_fft_to_dac))

# svr_to_out = get_paths('svr', 'out', connections, [])
# print(len(svr_to_out))

# svr_to_fft = get_paths('svr', 'fft', connections, ['out', 'dac'])
# print(len(svr_to_fft))

# inverted_svr_to_fft = get_paths('fft', 'svr', inverted_connections, ['out', 'dac']) # works
# print('inverted_svr_to_fft', inverted_svr_to_fft)
#
# inverted_fft_to_dac = get_paths('dac', 'fft', inverted_connections, ['out', 'svr'])
# print('inverted_fft_to_dac', inverted_fft_to_dac)
#
# inverted_svr_to_dac = get_paths('dac', 'svr', inverted_connections, ['out', 'fft'])
# print('inverted_svr_to_dac', inverted_svr_to_dac)
#
# inverted_dac_to_fft = get_paths('fft', 'dac', inverted_connections, ['out', 'svr'])
# print('inverted_dac_to_fft', inverted_dac_to_fft)
#
# inverted_fft_to_out = get_paths('out', 'fft', inverted_connections, ['dac', 'svr'])
# print('inverted_fft_to_out', inverted_fft_to_out)
#
# inverted_dac_to_out = get_paths('out', 'dac', inverted_connections, ['fft', 'svr'])
# print('inverted_dac_to_out', inverted_dac_to_out)

# svr_to_dac = get_paths('svr', 'dac', connections, ['fft', 'out'])
# print(len(svr_to_dac))


# fft_to_dac = get_paths('fft', 'dac', connections, ['out', 'svr'])
# print(len(fft_to_dac))

# inverted_fft_to_dac = get_paths('dac', 'fft', inverted_connections, ['out', 'svr']) #doesnt work
# print(len(inverted_fft_to_dac))

# inverted_dac_to_out = get_paths('out', 'dac', inverted_connections, ['fft', 'svr'])
# print(len(inverted_dac_to_out))

# fft_to_dac = get_paths('fft', 'dac', connections, ['out', 'svr'])
# print(len(fft_to_dac))
#
# dac_to_out = get_paths('dac', 'out', connections, ['svr', 'fft'])
# print(len(dac_to_out))
#
# svr_to_dac = get_paths('svr', 'dac', connections, ['out', 'fft'])
# print(len(svr_to_dac))
#
# dac_to_fft = get_paths('dac', 'fft', connections, ['out', 'svr'])
# print(len(dac_to_fft))

# svr_to_dac = get_paths('svr', 'dac', connections, ['out', 'fft'])
# print(len(svr_to_dac))
#
# inverted_dac_to_svr = get_paths('dac', 'svr', inverted_connections, ['out', 'fft'])
# print(len(inverted_dac_to_svr))

# inverted_dac_to_fft = get_paths('fft', 'dac', inverted_connections, ['out', 'svr'])
# print(len(inverted_dac_to_fft))


