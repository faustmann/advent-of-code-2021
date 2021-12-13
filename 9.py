import math


with open("9_1.txt") as fp:
    instance_lines = fp.readlines()

    headmap = list(map(lambda line: list(map(int, line.strip())), instance_lines))

def get_neighbour_min_value(x,y):
    neighbour_vals = []
    neighbour_offsets = [(1,0),(-1,0),(0,1),(0,-1)]
    for x_off, y_off in neighbour_offsets:
        neigh_x = x + x_off
        neigh_y = y + y_off
        if  0 <= neigh_x < len(headmap) and \
            0 <= neigh_y < len(headmap[0]):
            neighbour_vals.append(headmap[neigh_x][neigh_y])
    
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
        neighbour_offsets = [(1,0),(-1,0),(0,1),(0,-1)]
        for x_off, y_off in neighbour_offsets:
            neigh_x = x + x_off
            neigh_y = y + y_off

            if  0 <= neigh_x < len(headmap) and \
                0 <= neigh_y < len(headmap[0]) and \
                headmap[neigh_x][neigh_y] != 9:
                find_basin(neigh_x,neigh_y, basin_coord)         
    
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