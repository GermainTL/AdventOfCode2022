def test_example():
    assert solve_first_puzzle("example.txt") == 7
    assert solve_second_puzzle("example.txt") == "MCD"

def test_input():
    assert solve_first_puzzle("input.txt") == 1625
    assert solve_second_puzzle("input.txt") == "BPCZJLFJW"

def solve_first_puzzle(file_name):
    chars = parse_file(file_name)
    for i in range(len(chars)):
        window = chars[i:i+4];
        if len(window) == len(set(window)):
            return i + 4;

    return 'nope'

def solve_second_puzzle(file_name):
    chars = parse_file(file_name)
    for i in range(len(chars)):
        window = chars[i:i+14];
        if len(window) == len(set(window)):
            return i + 14;

    return 'nope'


def parse_file(file_name):
    with open(f"day6/input/{file_name}", "r") as file:
        line = file.read()

    return list(line);
