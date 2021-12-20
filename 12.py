from collections import defaultdict
from collections import Counter

neighbour_dict = defaultdict(list)


def import_connections_into_neighbour_dict(r_conn_lst):
    for end_p1, end_p2 in r_conn_lst:
        neighbour_dict[end_p1].append(end_p2)

        if end_p1 != "start" and end_p2 != "end":
            neighbour_dict[end_p2].append(end_p1)


with open("12_1.txt") as fp:
    instance_lines = fp.readlines()

    raw_connection_list = list(
        map(lambda line: line.strip().split("-"), instance_lines)
    )
    import_connections_into_neighbour_dict(raw_connection_list)

finished_paths = []


def travel_one_step(paths):
    all_new_part_paths = []
    for path in paths:
        if path[-1] != "end":
            double_visit_not_used = (
                max(Counter([stop for stop in path if stop.islower()]).values()) < 2
            )

            all_new_part_paths = all_new_part_paths + [
                path.copy() + [new_dst]
                for new_dst in neighbour_dict[path[-1]]
                if new_dst.isupper()
                or (
                    (not new_dst in path or double_visit_not_used)
                    and new_dst != "start"
                )
            ]
        else:
            finished_paths.append(path)

    return all_new_part_paths


found_paths = [["start"]]
for step in range(1000):
    print(f"steps: {step}")
    found_paths = travel_one_step(found_paths)
    if not found_paths:
        print("all paths closed")
        break

print(f"found paths {len(finished_paths)}")
