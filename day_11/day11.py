with open('day_11/seating_chart.txt') as f:
    seats = [x.strip() for x in f.readlines()]

seats = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL'
]

seats = [[y for y in x] for x in seats]


def check_adjacent(seating, row, col):
    occupied_count = 0
    for x in range(max(0, row - 1), min(row + 2, len(seating))):
        for y in range(max(0, col - 1), min(col + 2, len(seating[row]))):
            if seating[x][y] == '#' and (x, y) != (row, col):
                occupied_count += 1
    return occupied_count


while True:
    to_fill = []
    to_empty = []
    for i in range(len(seats)):
        for k in range(len(seats[i])):
            if seats[i][k] != '.':
                occupied = check_adjacent(seats, i, k)
                if seats[i][k] == 'L' and occupied == 0:
                    to_fill.append((i, k))
                elif seats[i][k] == '#' and occupied > 3:
                    to_empty.append((i, k))
    for fill_seat in to_fill:
        seats[fill_seat[0]][fill_seat[1]] = '#'
    for fill_seat in to_empty:
        seats[fill_seat[0]][fill_seat[1]] = 'L'
    if len(to_fill) + len(to_empty) == 0:
        break

print(sum(map(lambda x: x.count('#'), seats)))


def check_adj_2(seating, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(seating), len(seating[0])
    occupied_seats = 0
    for d in directions:
        x, y = row + d[0], col + d[1]
        while 0 <= x < rows and 0 <= y < cols:
            if seating[x][y] == '.':
                x, y = x + d[0], y + d[1]
            else:
                occupied_seats += 1 if seating[x][y] == '#' else 0
                break
    return occupied_seats


while True:
    to_fill = []
    to_empty = []
    for i in range(len(seats)):
        for k in range(len(seats[i])):
            if seats[i][k] != '.':
                occupied = check_adj_2(seats, i, k)
                if seats[i][k] == 'L' and occupied == 0:
                    to_fill.append((i, k))
                elif seats[i][k] == '#' and occupied > 4:
                    to_empty.append((i, k))
    for fill_seat in to_fill:
        seats[fill_seat[0]][fill_seat[1]] = '#'
    for fill_seat in to_empty:
        seats[fill_seat[0]][fill_seat[1]] = 'L'
    if len(to_fill) + len(to_empty) == 0:
        break

print(sum(map(lambda x: x.count('#'), seats)))

