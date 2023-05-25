import re;

def test_example():
    assert solve_first_puzzle('example.txt') == 'CMZ';

def test_input():
    assert solve_first_puzzle('input.txt') == 66616;

def solve_first_puzzle(file_name):
    [stacks, commands] = parse_file(file_name);

    return stacks;

def parse_file(file_name): 
    with open(f'day5/input/{file_name}', 'r') as file:
        lines = file.read().splitlines()
    
    separation_index = lines.index('');
    stacks = lines[:separation_index];
    stacks.reverse();
    stacks = stacks.pop(0).replace('[', '').replace(']', '').replace(' ', '');
    command_texts = lines[separation_index:];
    
    commands = [];
    for command_text in command_texts:
        commands.append([int(x) for x in re.findall(r'move ([0-9]) from ([0-9]) to ([0-9])', command_text)]);

    print(commands);
    
    return [stacks, commands];
