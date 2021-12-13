import math


with open("9_1.txt") as fp:
    instance_lines = fp.readlines()

    headmap = list(map(lambda line: list(map(int, line.strip())), instance_lines))

def get_neighbour_min_value(x,y):
    neighbour_vals = []
    if x-1 >= 0:
        neighbour_vals.append(headmap[x-1][y])
    if x+1 < len(headmap):
        neighbour_vals.append(headmap[x+1][y])
    if y-1 >= 0:
        neighbour_vals.append(headmap[x][y-1])
    if y+1 < len(headmap[0]):
        neighbour_vals.append(headmap[x][y+1])
    
    return min(neighbour_vals)

summed_risk_levels = sum([headmap[x][y]+1 
        for x in range(len(headmap)) 
        for y in range(len(headmap[0]))
        if get_neighbour_min_value(x,y) > headmap[x][y]
        ])

print(f'summed risk level {summed_risk_levels}')



def find_basin(x,y, basin_coord):
    old_basin_coord_len = len(basin_coord)
    basin_coord.add((x,y))

    if old_basin_coord_len != len(basin_coord):
        if x-1 >= 0 and headmap[x-1][y] != 9:
            find_basin(x-1,y, basin_coord)
        if x+1 < len(headmap) and headmap[x+1][y] != 9:
            find_basin(x+1,y, basin_coord)
        if y-1 >= 0 and headmap[x][y-1] != 9:
            find_basin(x,y-1, basin_coord)
        if y+1 < len(headmap[0]) and headmap[x][y+1] != 9:
            find_basin(x,y+1, basin_coord)
    
    return basin_coord

basins = sorted([find_basin(x,y,set([])) 
            for x in range(len(headmap)) 
            for y in range(len(headmap[0]))
            if get_neighbour_min_value(x,y) > headmap[x][y]
            ],
            key=lambda elem: len(elem),
            reverse=True
         )

result = 1
for fact in [len(basin) for basin in basins[:3]]:
    result = result * fact

print(f'result {result}')