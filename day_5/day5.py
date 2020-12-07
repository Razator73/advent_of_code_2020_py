with open('day_5/boarding_passes.txt') as f:
    boarding_passes = f.read().split('\n')

# part 1
seats = []
for boarding_pass in boarding_passes:
    row = (0, 127)
    for char in boarding_pass[:7]:
        rows = row[1] - row[0] + 1
        row = (row[0], row[1] - rows // 2) if char == 'F' else (row[0] + rows // 2, row[1])

    col = (0, 7)
    for char in boarding_pass[7:]:
        cols = col[1] - col[0] + 1
        col = (col[0], col[1] - cols // 2) if char == 'L' else (col[0] + cols // 2, col[1])

    # print((row[0], col[0]), row[0] * 8 + col[0])
    seats.append(row[0] * 8 + col[0])
print(f'The highest sead id is: {max(seats)}')

# part 2
available_seats = [x for x in range(min(seats), max(seats))]

possible_seats = []
print(f'The available seat is: {[x for x in available_seats if x not in seats and x + 1 in seats and x - 1 in seats]}')
