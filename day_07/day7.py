import re


# parse the bag rules
with open('day_7/bag_rules.txt') as f:
    bag_rules_text = f.read()

bag_rules = bag_rules_text.strip().split('\n')
bag_pattern = r'([a-z\s]+) bags contain ([^\.]+)\.'
contents_pattern = r'(\d+) ([a-z\s]+) bag'
rules = {}
for rule in bag_rules:
    if bag_search := re.search(bag_pattern, rule):
        bag, contents = bag_search.groups()
        rules.setdefault(bag, None)
        if contents := re.findall(contents_pattern, contents):
            rules[bag] = {x[1]: int(x[0]) for x in contents}


# part 1
def in_bag(outer_bag, find_bag):
    global rules
    if outer_bag is None:
        return False
    if find_bag in outer_bag.keys():
        return True
    inner_bags = []
    for inner_bag in outer_bag.keys():
        inner_bags.append(in_bag(rules[inner_bag], find_bag))
    return any(inner_bags)


count = 0
check_bag = 'shiny gold'
for bag, contents in rules.items():
    if in_bag(contents, check_bag):
        count += 1
print(f'{check_bag} can be found in {count} different bags')


# part 2
def count_bags(bag_contents):
    global rules
    if bag_contents is None:
        return 0
    total_count = sum(bag_contents.values())
    for inner_bag, inner_count in bag_contents.items():
        total_count += inner_count * count_bags(rules[inner_bag])
    return total_count


count_bag = 'shiny gold'
print(f'A {count_bag} contains {count_bags(rules[count_bag])} bags')
