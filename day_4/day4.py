import re
from pathlib import Path

passport_file = Path('day_4/passports.txt')
with open(passport_file) as f:
    passport_data = f.read()

passports = passport_data.split('\n\n')
passport_pattern = r'([^:]+):([^\s\n]+)[\s\n]?'
passports = [{key: val for key, val in re.findall(passport_pattern, passport)} for passport in passports]

required_keys = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

# part one
good_count = 0
for passport in passports:
    if not [x for x in required_keys if x not in passport.keys()]:
        good_count += 1
print(f'There are {good_count} good passports.')


# part two
def hgt_validator(hgt):
    if hgt_search := re.search(r'(\d+)(in|cm)', hgt):
        hgt_num, hgt_units = int(hgt_search.group(1)), hgt_search.group(2)
        return (150 <= hgt_num <= 193) if hgt_units == 'cm' else (59 <= hgt_num <= 76)
    return False


validator = {'byr': lambda x: 1920 <= int(x) <= 2002,
             'iyr': lambda x: 2010 <= int(x) <= 2020,
             'eyr': lambda x: 2020 <= int(x) <= 2030,
             'hgt': hgt_validator,
             'hcl': lambda x: re.search(r'#[0-9a-f]{6}', x) and len(x) == 7,
             'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
             'pid': lambda x: re.search(r'\d{9}', x) and len(x) == 9,
             'cid': lambda x: True}
good_count = 0
for passport in passports:
    if not [x for x in required_keys if x not in passport.keys()]:
        valid = True
        passport_check = []
        for k, v in passport.items():
            if not validator[k](v):
                valid = False
                break
        good_count += 1 if valid else 0
print(f'There are {good_count} good passports with validation.')
