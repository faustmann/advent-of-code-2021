with open("11_1.txt") as fp:
    instance_lines = fp.readlines()

    octopuses_map = list(map(lambda line: list(map(int, line.strip())), instance_lines))

num_flashes = 0


def prop_flash_oct_counted(x, y, oct_map):
    global num_flashes

    offset_range = [-1, 0, 1]
    neighbour_offsets = [
        (x_off, y_off)
        for x_off in offset_range
        for y_off in offset_range
        if not (x_off == 0 and y_off == 0)
    ]
    for x_off, y_off in neighbour_offsets:
        neigh_x = x + x_off
        neigh_y = y + y_off
        if (
            0 <= neigh_x < len(oct_map)
            and 0 <= neigh_y < len(oct_map[0])
            and oct_map[neigh_x][neigh_y] != 10
        ):
            oct_map[neigh_x][neigh_y] = oct_map[neigh_x][neigh_y] + 1

            if oct_map[neigh_x][neigh_y] == 10:
                num_flashes = num_flashes + 1
                prop_flash_oct_counted(neigh_x, neigh_y, oct_map)


def next_step_inc(oct_map):
    global num_flashes

    intermediate_oct_map = [[oct + 1 for oct in oct_line] for oct_line in oct_map]

    flash_starter_coords = [
        (x, y)
        for x in range(len(oct_map))
        for y in range(len(oct_map[0]))
        if intermediate_oct_map[x][y] == 10
    ]

    num_flashes = num_flashes + len(flash_starter_coords)

    for x, y in flash_starter_coords:
        prop_flash_oct_counted(x, y, intermediate_oct_map)

    final_oct_map = [
        [oct % 10 for oct in oct_line] for oct_line in intermediate_oct_map
    ]

    return final_oct_map


for step in range(1000):
    octopuses_map = next_step_inc(octopuses_map)
    if all([oct == 0 for oct_line in octopuses_map for oct in oct_line]):
        break

print(f"all flash {step+1}")
