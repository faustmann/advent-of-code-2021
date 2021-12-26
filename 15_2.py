import sys
import heapq
from collections import namedtuple


Point = namedtuple("Point", "x y")

with open("15_1.txt") as fp:
    risk_map = fp.read().splitlines()

x1_len = len(risk_map[0])
y1_len = len(risk_map)
x_len = x1_len * 5
y_len = y1_len * 5
start_pos = Point(0, 0)
end_pos = Point(x_len - 1, y_len - 1)

openlist = []
heapq.heappush(openlist, (0, start_pos))
min_cost_map = [[(sys.maxsize, None) for y in range(y_len)] for x in range(x_len)]
min_cost_map[0][0] = (0, None)


def get_cost_to_enter_node(pos):
    x, y = pos
    risk_summand = x // x1_len + y // y1_len
    risk_val_curr_pos = int(risk_map[y % y1_len][x % x1_len]) + risk_summand
    risk_val_curr_pos = (
        (risk_val_curr_pos % 10) + 1 if risk_val_curr_pos >= 10 else risk_val_curr_pos
    )

    return risk_val_curr_pos


get_cost_to_enter_node((2, y1_len))


def heuristic_manhattan_dist(pos):
    x, y = pos
    return (x_len - 1 - x) + (y_len - 1 - y)


def expand_pos(cur_pos):
    x, y = cur_pos
    two_d_offsets = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    for x_off, y_off in two_d_offsets:
        new_pos = Point(x + x_off, y + y_off)
        if 0 <= new_pos.x < x_len and 0 <= new_pos.y < y_len:
            if min_cost_map[new_pos.x][new_pos.y][1] != None:
                continue

            new_part_cost = min_cost_map[cur_pos.x][cur_pos.y][
                0
            ] + get_cost_to_enter_node(new_pos)

            new_pos_elem_in_openlist = next(
                (elem for elem in openlist if elem[1] == new_pos), None
            )

            if (
                new_pos_elem_in_openlist != None
                and new_part_cost > min_cost_map[new_pos.x][new_pos.y][0]
            ):
                continue

            min_cost_map[new_pos.x][new_pos.y] = (new_part_cost, cur_pos)

            if new_pos == end_pos:
                return False

            heapq.heappush(
                openlist, (new_part_cost + heuristic_manhattan_dist(new_pos), new_pos)
            )

    return True


while len(openlist) > 0:
    print(f"len openlist {len(openlist)}")
    _, current_pos = heapq.heappop(openlist)
    if not expand_pos(current_pos):
        break

cur_rev_path_pos = end_pos
while cur_rev_path_pos != start_pos:
    cost, pred = min_cost_map[cur_rev_path_pos.x][cur_rev_path_pos.y]
    print((cost, pred))
    cur_rev_path_pos = pred

print(f"min route cost {min_cost_map[end_pos.x][end_pos.y]}")
