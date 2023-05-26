def test_example():
    assert solve_first_puzzle("example.txt") == 24000
    assert solve_second_puzzle("example.txt") == 45000


def test_input():
    assert solve_first_puzzle("input.txt") == 66616
    assert solve_second_puzzle("input.txt") == 199172


def solve_first_puzzle(file_name):
    lines = parse_file(file_name)

    elves_calories = get_all_elves_calories(lines)
    max_calories = max(elves_calories)

    return max_calories


def solve_second_puzzle(file_name):
    lines = parse_file(file_name)

    elves_calories = get_all_elves_calories(lines)
    elves_calories.sort()

    return sum(elves_calories[-3:])


def get_all_elves_calories(lines):
    elves_calories = []
    sum_index = 0
    for line in lines:
        if line == "\n":
            sum_index += 1
        else:
            calories = int(line.replace("\n", ""))
            try:
                elves_calories[sum_index] += calories
            except IndexError:
                elves_calories.insert(sum_index, calories)

    return elves_calories


def parse_file(file_name):
    file = open(f"day1/input/{file_name}", "r")

    return file.readlines()
