with open('day_9/cypher_data.txt') as f:
    encoded_data = [int(x.strip()) for x in f.readlines()]

# part 1
preamble_len = 25
invalid_num = i = 0
valid = False
for i in range(preamble_len, len(encoded_data)):
    invalid_num = encoded_data[i]
    for k in range(i - preamble_len, i):
        num_one = encoded_data[k]
        valid = False
        for num_two in (encoded_data[i - preamble_len: k] + encoded_data[k + 1: preamble_len]):
            if num_one + num_two == invalid_num:
                valid = True
                break
        if valid:
            break
    if not valid:
        break
print(f'The first invalid number is {invalid_num} found at index {i}')

# part 2
k = i = 0
for i in range(len(encoded_data)):
    sum_total = encoded_data[i]
    k = i + 1
    while k < len(encoded_data) and sum_total < invalid_num:
        sum_total += encoded_data[k]
        k += 1
    if sum_total == invalid_num:
        break
min_weak_num, max_weak_num = min(encoded_data[i: k]), max(encoded_data[i: k])
print(f'The min is {min_weak_num} and the max is {max_weak_num} giving weakness of {min_weak_num + max_weak_num}')
