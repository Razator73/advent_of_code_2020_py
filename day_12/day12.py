import re

with open('day_12/nav_instructions.txt') as f:
    nav_instructions = f.read().split('\n')

instruc_pattern = r'([NSEWLRF])(\d+)'
convert = {0: 'E', 1: 'N', 2: 'W', 3: 'S'}
directions = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}

# part 1
ship_loc = [0, 0]
ship_direc = 0
for instruc in nav_instructions:
    if instruc_search := re.search(instruc_pattern, instruc):
        command = instruc_search.group(1)
        amount = int(instruc_search.group(2))
        if command in 'RL':
            left_right = 1 if command == 'L' else -1
            ship_direc += (left_right * amount // 90)
            ship_direc %= 4
        elif command in 'NESW':
            ship_loc[0] += amount * directions[command][0]
            ship_loc[1] += amount * directions[command][1]
        elif command == 'F':
            ship_loc[0] += amount * directions[convert[ship_direc]][0]
            ship_loc[1] += amount * directions[convert[ship_direc]][1]
print(f'The ship\'s Manhattan distances is {abs(ship_loc[0]) + abs(ship_loc[1])}.')

# part 2
ship_loc = [0, 0]
waypoint_loc = [10, 1]
waypoint_rotations = {0: lambda x, y: [x, y],
                      1: lambda x, y: [-y, x],
                      2: lambda x, y: [-x, -y],
                      3: lambda x, y: [y, -x]}
for instruc in nav_instructions:
    if instruc_search := re.search(instruc_pattern, instruc):
        command = instruc_search.group(1)
        amount = int(instruc_search.group(2))
        if command in 'RL':
            rotation = (amount // 90) % 4 if command == 'L' else (-1 * amount // 90) % 4
            waypoint_loc = waypoint_rotations[rotation](*waypoint_loc)
        elif command in 'NESW':
            waypoint_loc[0] += amount * directions[command][0]
            waypoint_loc[1] += amount * directions[command][1]
        elif command == 'F':
            ship_loc[0] += amount * waypoint_loc[0]
            ship_loc[1] += amount * waypoint_loc[1]
print(f'The ship\'s Manhattan distances is {abs(ship_loc[0]) + abs(ship_loc[1])}.')
