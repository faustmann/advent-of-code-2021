def prepare_1st_line(line):
    return list(map(int,line.split(',')))

def prepare_bingo_lines(lines):
    return [int(elem) for line in lines for elem in line.split(' ') if elem.isnumeric()]

with open("4_1.txt") as fp:
    instance_lines = fp.readlines()
    random_values = prepare_1st_line(instance_lines[0])

    bingo_instances = []
    current_buffer = []
    for line in instance_lines[2:]:
        if line == '\n':
            bingo_instances.append(prepare_bingo_lines(current_buffer))
            current_buffer = []
        current_buffer.append(line.strip())

def mark_number(check_for_value, current_number):
    if check_for_value == current_number:
        return -current_number
    else:
        return current_number

def check_vertical(bingo_instance):
    completed_vertical_lines = [completed_vertical_line for completed_vertical_line in
        [bingo_instance[i:i+5] for i in range(0, len(bingo_instance), 5) ] 
        if all(val < 0 for val in completed_vertical_line)
    ]

    return len(completed_vertical_lines) != 0

def check_horizontal(bingo_instance):
    
    horizontal_index_groups =[ [offset + (i*5) for i in range(5) ]  for offset in range(5)]
    horizontal_groups = []

    for horizontal_index_group in horizontal_index_groups:
        horizontal_groups.append(list(map(lambda cur_inde: bingo_instance[cur_inde],horizontal_index_group)))
    
    completed_horizontal_lines = [horizontal_group for horizontal_group in
        horizontal_groups
        if all(val < 0 for val in horizontal_group)
    ]

    return len(completed_horizontal_lines) != 0

on_fire = False
for random_value in random_values:
    bingo_instances = [list(map(lambda cur_val:  mark_number(random_value, cur_val),bingo_instance)) for bingo_instance in bingo_instances]

    if not on_fire:
        unfinished_bingo_instances = [bingo_instance for bingo_instance in bingo_instances if not check_vertical(bingo_instance) and not check_horizontal(bingo_instance)]
        if len(unfinished_bingo_instances) ==1:
            print('ende')
            on_fire = True
            bingo_instances = unfinished_bingo_instances
    else:
        finished_bingo_instances = [bingo_instance for bingo_instance in bingo_instances if check_vertical(bingo_instance) or check_horizontal(bingo_instance)]
        if len(finished_bingo_instances) ==1:
            result = sum([unmarked_spots for unmarked_spots in finished_bingo_instances[0] if unmarked_spots > 0]) * random_value
            print(result)
            break

print('fin')