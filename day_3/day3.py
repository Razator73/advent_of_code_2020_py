from pathlib import Path

slope_file = Path('day_3/slope.txt')
with open(slope_file) as f:
    slope_data = [x.strip() for x in f.readlines()]

# part 1
tree_count = 0
pos = 0
for row in slope_data:
    if row[pos] == '#':
        tree_count += 1
    pos += 3
    pos %= len(row)
print(f'Total trees hit: {tree_count}')

# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []
for slope in slopes:
    right, down = slope
    tree_count = pos = 0
    for row in slope_data[::down]:
        if row[pos] == '#':
            tree_count += 1
        pos += right
        pos %= len(row)
    trees.append(tree_count)
tree_prod = 1
for tree in trees:
    tree_prod *= tree
tree_str = ' * '.join([str(tree) for tree in trees])
print(f'{tree_str} = {tree_prod}')
