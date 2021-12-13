from statistics import median, mean

with open("7_1.txt") as fp:
    instance_lines = fp.readlines()

    heights = list(map(int, instance_lines[0].split(',')))

optimal_pos = median(heights)

complete_traveled_dist = sum([abs(height - optimal_pos) for height in heights])
    
print(f'total distance to median height {complete_traveled_dist}')

optimal_pos = int(mean(heights))

def fuel_to_travel(dist):
    return (dist+1) * dist /2

complete_traveled_dist = sum([fuel_to_travel(abs(height - optimal_pos)) for height in heights])
    
print(f'total fuel to reach mean height {complete_traveled_dist}')