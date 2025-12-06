with open("input.txt") as file:
    data = file.read()


fresh_str, available_str = data.split('\n\n')

fresh = fresh_str.splitlines()
available = available_str.splitlines()

fresh_ranges = [range(int(rng.split('-')[0]), int(rng.split('-')[1]) + 1) for rng in fresh]

counter = 0

for a in available:
    for fr in fresh_ranges:
        if int(a) in fr:
            counter += 1
            break


print(counter)
