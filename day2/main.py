score_by_shape = {
    'X': 1,
    'Y': 2,
    'Z': 3,
};

winning_combinations = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
};

draw_combinations = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
};

lose_combinations = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
};

def test_example():
    assert solve_first_puzzle('example.txt') == 15;
    assert solve_second_puzzle('example.txt') == 12;

def test_input():
    assert solve_first_puzzle('input.txt') == 15337;
    assert solve_second_puzzle('input.txt') == 11696;

def solve_first_puzzle(file_name):
    lines = parse_file(file_name);
    
    total_points = 0;
    for line in lines:
        round = line.split();
        total_points += score_by_shape[round[1]];
        if round[1] == winning_combinations[round[0]]:
            total_points += 6;
        elif round[1] == draw_combinations[round[0]]:
            total_points += 3;
    
    return total_points;

def solve_second_puzzle(file_name):
    lines = parse_file(file_name);

    total_points = 0;
    for line in lines:
        round = line.split();
        should_lose = round[1] == 'X';
        should_draw = round[1] == 'Y';
        if should_lose:
            total_points += score_by_shape[lose_combinations[round[0]]];
        elif should_draw:
            total_points += score_by_shape[draw_combinations[round[0]]];
            total_points += 3;
        else:
            total_points += score_by_shape[winning_combinations[round[0]]];
            total_points += 6;

    return total_points;

def parse_file(file_name): 
    file = open(f'day2/input/{file_name}', 'r');
    
    return file.readlines();
