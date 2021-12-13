def prepare_lines(line):
    return [list(map(int,coord.split(','))) for coord in line.split('->')]

with open("5_1.txt") as fp:
    instance_lines = fp.readlines()

    pipes = list(map(prepare_lines, instance_lines))


straight_pipe_coords = [pipe_coordinates for pipe_coordinates in pipes 
    # if pipe_coordinates[0][0] == pipe_coordinates[1][0] 
    # or pipe_coordinates[0][1] == pipe_coordinates[1][1]
    ] 

max_x = max([x for pipe_coordinates in straight_pipe_coords for x in [pipe_coordinates[0][0], pipe_coordinates[1][0]]])
max_y = max([y for pipe_coordinates in straight_pipe_coords for y in [pipe_coordinates[0][1], pipe_coordinates[1][1]]])


crossing_map = [[0 for y in  range(max_y+1) ] for x in range(max_x+1)]
crossings = 0
for [[x_1, y_1], [x_2, y_2]] in straight_pipe_coords: 
    left_point = [x_1, y_1] if x_1 <= x_2 else [x_2, y_2]
    right_point = [x_1, y_1] if x_1 > x_2 else [x_2, y_2]
    [top_left_point, other_point] = [right_point, left_point] if left_point[0] == right_point[0] and left_point[1] > right_point[1] else [left_point, right_point]
    
    y_forward = True if other_point[1] > top_left_point[1] else False

    x_positions = list(range(top_left_point[0], other_point[0]+1))

    if y_forward:
        y_positions = list(range(top_left_point[1], other_point[1]+1))
    else:
        y_positions = list(reversed(range(other_point[1], top_left_point[1]+1)))

    if len(x_positions) == 1:
        x_positions = x_positions * len(y_positions)
    elif len(y_positions) == 1:
        y_positions = y_positions * len(x_positions)
    
    for x,y in zip(x_positions, y_positions):
        crossing_map[x][y] = crossing_map[x][y]+1

        if crossing_map[x][y] == 2:
            crossings = crossings +1

print(f'fin {crossings}')