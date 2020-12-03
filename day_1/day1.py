from pathlib import Path

expense_file = Path('day_1/expense_report.txt')
with open(expense_file) as f:
    expense_data = [int(x.strip()) for x in f.readlines()]

# part one
n = len(expense_data)
for i in range(n):
    current_num = expense_data[i]
    for num in expense_data[i + 1:]:
        if current_num + num == 2020:
            print(f'{current_num} * {num} = {current_num * num}')

# part two
for i in range(n):
    num_one = expense_data[i]
    for k in range(i + 1, n):
        num_two = expense_data[k]
        if num_one + num_two < 2020:
            for num_three in expense_data[k + 1:]:
                if sum(nums := [num_one, num_two, num_three]) == 2020:
                    print(' * '.join([str(num) for num in nums]) + f' = {num_one * num_two * num_three}')
