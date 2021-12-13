
with open("1_1.txt") as fp:
    depth_values = list(map(int, fp.readlines()))

count_increase = 0
checks=0
for current_depth, next_depth in zip(depth_values, depth_values[1:]):
    if current_depth < next_depth:
        count_increase = count_increase +1
    checks = checks +1

print(f'simple count increase {count_increase}')


def sliding_3window(start_index, values):
    return values[start_index] + values[start_index +1] + values[start_index +2]

count_increase = 0
depth_values_sliding = [sliding_3window(index, depth_values) for index in range(len(depth_values)-2)]
for current_depth, next_depth in zip(depth_values_sliding, depth_values_sliding[1:]):
    if current_depth < next_depth:
        count_increase = count_increase +1

print(f'sliding count increase {count_increase}')