import re

with open('day_8/boot_instructions.txt') as f:
    boot_instr_str = f.read()
boot_instructions = boot_instr_str.strip().split('\n')

# part 1
accumulator = current_command = 0
run_commands = []
while current_command not in run_commands:
    run_commands.append(current_command)
    command, modifier = re.search(r'(acc|jmp|nop) ([+-]\d+)', boot_instructions[current_command]).groups()
    current_command += int(modifier) if command == 'jmp' else 1
    accumulator += int(modifier) if command == 'acc' else 0
print(f'The accumulator is at {accumulator}')

# part 2
changed_command = changed_command_str = ''
for i in range(len(boot_instructions)):
    accumulator = current_command = 0
    run_commands = []
    while current_command not in run_commands and current_command != len(boot_instructions):
        run_commands.append(current_command)
        command, modifier = re.search(r'(acc|jmp|nop) ([+-]\d+)', boot_instructions[current_command]).groups()
        if command in ('jmp', 'nop'):
            if i == 0:
                command = 'jmp' if command == 'nop' else 'nop'
                changed_command = current_command
                changed_command_str = boot_instructions[current_command]
            i -= 1
        current_command += int(modifier) if command == 'jmp' else 1
        accumulator += int(modifier) if command == 'acc' else 0
    if current_command == len(boot_instructions):
        break
print(f'The accumulator is at {accumulator}.\n'
      f'Boot is fixed by changing the command at index {changed_command} ({changed_command_str})')
