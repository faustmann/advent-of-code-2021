from collections import namedtuple

Node = namedtuple("Node", "l r")


def treeify(part_instance_line, side="l"):
    cur_idx = part_instance_line[0]
    l = None
    r = None

    while part_instance_line[cur_idx] != "]":
        if part_instance_line[cur_idx] == "[":
            return treeify(part_instance_line[1])
        elif part_instance_line[cur_idx].isnumeric() and side == "l":
            number, rest = part_instance_line[cur_idx:].split(",", 1)
            l = int(number)
            r = treeify(rest, "r")

            return Node(l, r)
        elif part_instance_line[cur_idx].isnumeric() and side == "r":
            number, _ = part_instance_line[cur_idx:].split("]", 1)
            r = int(number)
            return r


with open("18_1.txt") as fp:
    instance_lines = fp.readlines()

    s_numbers = list(map(treeify, instance_lines))
