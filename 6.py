def next_fishday(fish_state):
    (stage, amount) = fish_state
    if stage == 0:
        return [(8, amount), (6, amount)]
    else:
        return [(stage -1, amount)]


with open("6_1.txt") as fp:
    instance_lines = fp.readlines()

    fishes = list(map(int, instance_lines[0].split(',')))

    fishes_dict = {}
    for fish in fishes:
        if not fish in fishes_dict:
            fishes_dict[fish] = 0
        fishes_dict[fish] = fishes_dict[fish] +1
fishes_dict = fishes_dict.items()


for day in range(256):
    print(f'day {day}')
    fishes_dict = [new_fished for old_fish in fishes_dict for new_fished in next_fishday(old_fish)]
    
    new_fish_dict = {}
    for (stage, amount) in fishes_dict:
        if not stage in new_fish_dict:
            new_fish_dict[stage] = 0
        new_fish_dict[stage] = new_fish_dict[stage] +amount 
    fishes_dict = new_fish_dict.items()

print(f'num of fishes {sum([fishamount for (_, fishamount) in fishes_dict])}')

