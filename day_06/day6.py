with open('day_6/responses.txt') as f:
    responses_text = f.read().strip()

responses = [x.split('\n') for x in responses_text.split('\n\n')]

# part 1
counts = 0
for group in responses:
    group_counts = len(list(set([x for x in ''.join(group)])))
    counts += group_counts
print(f'The sum of the counts is: {counts}')

# part 2
counts = 0
for group in responses:
    group_count = 0
    for response in group[0]:
        count = True
        for others in group[1:]:
            if response not in [x for x in others]:
                count = False
                break
        group_count += 1 if count else 0
    counts += group_count

print(f'The sum of the counts is: {counts}')
