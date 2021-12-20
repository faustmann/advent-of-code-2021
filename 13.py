with open("13_1.txt") as fp:
    instance_lines = fp.read()

    raw_coordinates, raw_instructions = instance_lines.split("\n\n")
    coordinates = set(
        map(lambda elem: tuple(map(int, elem.split(","))), raw_coordinates.split("\n"))
    )
    instructions = list(
        map(lambda elem: elem.split(" ")[-1].split("="), raw_instructions.split("\n"))
    )


def handle_fold(instruction, coordinate):
    axis, fold_pos = instruction
    fold_pos = int(fold_pos)
    if axis == "x":
        return (fold_pos - abs(coordinate[0] - fold_pos), coordinate[1])
    else:
        return (coordinate[0], fold_pos - abs(coordinate[1] - fold_pos))


points = coordinates
for instruction in instructions:
    points = {handle_fold(instruction, coordinate) for coordinate in points}


print(f"number of points {len(points)}")


def print_point_cloud(plot_points):
    max_x = max(map(lambda elem: elem[0], plot_points))
    max_y = max(map(lambda elem: elem[1], plot_points))

    plane = [("." * (max_x + 1))].copy() * (max_y + 1)

    for x, y in plot_points:
        plane[y] = plane[y][:x] + "#" + plane[y][x + 1 :]

    print("\n".join(plane))


print_point_cloud(points)
