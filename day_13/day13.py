from math import ceil

with open('day_13/bus_schedule.txt') as f:
    bus_schedule = f.read().split('\n')

# bus_schedule = ['939', '7,13,x,x,59,x,31,19']

arrival_time = int(bus_schedule[0])
running_buses = [int(bus) for bus in bus_schedule[1].split(',') if bus != 'x']

# part 1
min_wait = max(running_buses)
first_bus = 0
for bus in running_buses:
    wait_time = (bus - arrival_time) % bus
    if wait_time < min_wait:
        min_wait, first_bus = wait_time, bus
print(f'For bus {first_bus} the wait is {min_wait} which is the shortest. Giving: {first_bus * min_wait}')


# part 2

# bus_schedule = ['', '7,13,x,x,59,x,31,19']
# bus_schedule= ['939', '17,x,13,19']
# bus_schedule = ['939', '67,7,59,61']
# bus_schedule = ['939', '67,x,7,59,61']
# bus_schedule = ['939', '67,7,x,59,61']
# bus_schedule = ['939', '1789,37,47,1889']
buses = bus_schedule[1].split(',')
a_dict = {}
zero_bus = int(buses[0])
for i in range(1, len(buses)):
    if buses[i] != 'x':
        bus = int(buses[i])
        a = 0
        while (zero_bus * a + i) % bus != 0:
            a += 1
        a_dict[bus] = a
while len(set(a_dict.values())) > 1:
    current_max = max(a_dict.values())
    for k, v in a_dict.items():
        if v < current_max:
            a_dict[k] += ceil((current_max - v) / k) * k

t = list(a_dict.values())[0] * zero_bus
print(f'The first such t is {t}')
