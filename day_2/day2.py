import re

with open('day_2/passwords.txt') as f:
    passwords = [x.strip() for x in f.readlines()]
password_pattern = r'(\d+)-(\d+)\s(\w):\s([a-zA-Z]+)'

# part one
good_count = 0
for password in passwords:
    if password_search := re.search(password_pattern, password):
        min_amount, max_amount, required_char, password_str = password_search.groups()
        min_amount, max_amount = int(min_amount), int(max_amount)
        char_dict = {}
        for char in password_str:
            char_dict.setdefault(char, 0)
            char_dict[char] += 1
        if min_amount <= char_dict.get(required_char, 0) <= max_amount:
            good_count += 1
print(f'There are {good_count} good passwords')

# part two
good_count = 0
for password in passwords:
    if password_search := re.search(password_pattern, password):
        position_1, position_2, required_char, password_str = password_search.groups()
        position_1, position_2 = int(position_1) - 1, int(position_2) - 1
        pos_1_char, pos_2_char = password_str[position_1], password_str[position_2]
        if (pos_1_char == required_char or pos_2_char == required_char) and pos_1_char != pos_2_char:
            good_count += 1
print(f'There are {good_count} good passwords')
