with open('day_10/joltage_adaptors.txt') as f:
    adaptors = [int(x) for x in f.readlines()]

adaptors = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

adaptors = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11,
            1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

adaptors.sort()

# part 1
jolt_diffs = {1: 0, 2: 0, 3: 1}
current_joltage = 0
for adaptor in adaptors:
    jolt_diffs[adaptor - current_joltage] += 1
    current_joltage = adaptor
print(f'1-jolt diffs = {jolt_diffs[1]} 3-jolt diffs = {jolt_diffs[3]} giving {jolt_diffs[1] * jolt_diffs[3]}')


# part 2
def array_memoization(func):
    memo = {}

    def helper(array, min_key):
        memo_key = (tuple(array), min_key)
        if memo_key not in memo:
            memo[memo_key] = func(array, min_key)
        return memo[memo_key]
    return helper


@array_memoization
def count_adaptor_array(sorted_adaptors, min_adaptor):
    if not sorted_adaptors:
        return 1
    count = 0
    k = 0
    while k < len(sorted_adaptors) and 0 < sorted_adaptors[k] - min_adaptor <= 3:
        k += 1
        count += count_adaptor_array(sorted_adaptors[k:], sorted_adaptors[k - 1])

    return count


print(count_adaptor_array(adaptors, 0))
