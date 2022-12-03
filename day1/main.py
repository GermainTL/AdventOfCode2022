def test_example():
    assert solve('example.txt') == 24000;

def test_input():
    assert solve('input.txt') == 66616;

def solve(file_name):
    lines = parse_file(file_name);
    
    all_sums = [];
    sum_index = 0;
    for line in lines:
        if line == '\n':
            sum_index += 1;
        else:
            calories = int(line.replace('\n', ''));
            try:
                all_sums[sum_index] += calories;
            except IndexError:
                all_sums.insert(sum_index, calories);

    max_calories = max(all_sums);
    return max_calories;

def parse_file(file_name): 
    file = open(f'day1/input/{file_name}', 'r');
    
    return file.readlines();
