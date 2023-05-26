import re


def test_example():
    assert solve_first_puzzle("example.txt") == "CMZ"
    assert solve_second_puzzle("example.txt") == "MCD"

def test_input():
    assert solve_first_puzzle("input.txt") == "QNHWJVJZW"
    assert solve_second_puzzle("input.txt") == "BPCZJLFJW"

def solve_second_puzzle(file_name):
    [stacks, commands] = parse_file(file_name)

    for command in commands[1:]:
        item_to_remove_count = int(command[0])
        remove_stack = int(command[1])
        add_stack = int(command[2])
        stacks[add_stack].extend(stacks[remove_stack][-item_to_remove_count:])
        stacks[remove_stack] = stacks[remove_stack][:-item_to_remove_count]
        
    result = []
    for stack_name in stacks:
        result.append(stacks[stack_name][-1])

    return "".join(result)

def solve_first_puzzle(file_name):
    [stacks, commands] = parse_file(file_name)

    for command in commands[1:]:
        item_to_remove_count = int(command[0])
        remove_stack = int(command[1])
        add_stack = int(command[2])
        for _ in range(item_to_remove_count):
            stacks[add_stack].append(stacks[remove_stack].pop())

    result = []
    for stack_name in stacks:
        result.append(stacks[stack_name][-1])

    return "".join(result)


def parse_file(file_name):
    with open(f"day5/input/{file_name}", "r") as file:
        lines = file.read().splitlines()

    separation_index = lines.index("")

    raw_stacks = lines[: separation_index - 1]
    raw_stack_names = lines[separation_index - 1]

    stacks = dict(
        zip(
            [int(i) for i in raw_stack_names.split()],
            [[] for _ in raw_stack_names.split()],
        )
    )

    for raw_stack in raw_stacks:
        for j in stacks:
            index = raw_stack_names.index(str(j))
            value = raw_stack[index]

            if value.strip():
                stacks[j].insert(0, value.strip())

    command_texts = lines[separation_index:]
    commands = []
    for command_text in command_texts:
        commands.append(
            list(
                *[
                    x
                    for x in re.findall(
                        r"move ([0-9]*) from ([0-9]*) to ([0-9]*)", command_text
                    )
                ]
            )
        )

    return [stacks, commands]
