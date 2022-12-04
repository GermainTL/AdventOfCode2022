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

def test_example():
    assert solve_first_puzzle('example.txt') == 15;

def test_input():
    assert solve_first_puzzle('input.txt') == 15337;

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

def parse_file(file_name): 
    file = open(f'day2/input/{file_name}', 'r');
    
    return file.readlines();
