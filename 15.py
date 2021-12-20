import sys

with open("15_1.txt") as fp:
    risk_map = fp.read().splitlines()

x_len = len(risk_map[0])
y_len = len(risk_map)
end_pos = (x_len - 1, y_len - 1)


def get_valid_neighbours(part_path, cost):
    x, y = part_path[-1]
    two_d_offsets = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    valid_neighbours = []
    for x_off, y_off in two_d_offsets:
        new_x = x + x_off
        new_y = y + y_off
        if (
            0 <= new_x < x_len
            and 0 <= new_y < y_len
            and not (new_x, new_y) in part_path
        ):
            new_cost = cost + int(risk_map[new_x][new_y])
            if new_cost < min_cost_map[new_x][new_y]:
                valid_neighbours.append(((new_x, new_y), new_cost))
                min_cost_map[new_x][new_y] = new_cost

    return valid_neighbours


finished_paths = []


def travel_one_step(paths):
    all_new_part_paths = []
    for path, cost in paths:
        if path[-1] != end_pos:
            all_new_part_paths = all_new_part_paths + [
                (path.copy() + [new_dst], new_cost)
                for (new_dst, new_cost) in get_valid_neighbours(path, cost)
            ]
        else:
            finished_paths.append((path, cost))

    return all_new_part_paths


min_cost_map = [[sys.maxsize for y in range(y_len)] for x in range(x_len)]

found_paths = [([(0, 0)], 0)]
for step in range(1000):
    print(f"step {step} found paths {len(found_paths)}")
    found_paths = travel_one_step(found_paths)

    if not found_paths:
        break


min_cost = min(map(lambda elem: elem[1], finished_paths))
print(f"min route cost {min_cost}")
