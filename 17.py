import math


with open("17_1.txt") as fp:
    instance_lines = fp.readlines()

    x_box_range, y_box_range = list(
        map(
            lambda raw_range: list(map(int, raw_range.split("=")[1].split(".."))),
            instance_lines[0][14:].split(", "),
        )
    )

# based on gaussian sum formula and pq formula to solve quadratic equation
v_x_min = math.ceil(-1 + math.sqrt(1 / 4 + 2 * x_box_range[0]))

if y_box_range[1] < 0:
    v_y_max = abs(y_box_range[0]) - 1

# part one answer
print(f"highest y pos {(v_y_max/2) * (v_y_max+1)}")

# start part two


def valid_help_rec(pos_x, pos_y, v_x, v_y):
    if (
        x_box_range[0] <= pos_x <= x_box_range[1]
        and y_box_range[0] <= pos_y <= y_box_range[1]
    ):
        return True
    elif pos_x <= x_box_range[1] and pos_y > y_box_range[0]:
        return valid_help_rec(pos_x + v_x, pos_y + v_y, max(v_x - 1, 0), v_y - 1)
    else:
        return False


def valid(v_x, v_y):
    return valid_help_rec(0, 0, v_x, v_y)


pos_vs = [
    (v_x, v_y)
    for v_x in range(v_x_min, x_box_range[1] + 1)
    for v_y in range(y_box_range[0], v_y_max + 1)
    if valid(v_x, v_y)
]

print(f"len {len(pos_vs)}")
