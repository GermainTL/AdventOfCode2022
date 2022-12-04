from curses.ascii import isupper

def test_example():
    assert solve_first_puzzle('example.txt') == 157;
    assert solve_second_puzzle('example.txt') == 70;

def test_input():
    assert solve_first_puzzle('input.txt') == 8139;
    assert solve_second_puzzle('input.txt') == 2668;

def solve_first_puzzle(file_name):
    lines = parse_file(file_name);

    total = 0;
    for line in lines:
        first_rucksack_part, second_rucksack_part = line[:len(line)//2], line[len(line)//2:];
        for char in first_rucksack_part:
            if second_rucksack_part.count(char) != 0:
                if isupper(char):
                    total += ord(char) - 64 + 26; # ASCII 'A' index is 65
                else:
                    total += ord(char) - 96; # ASCII 'a' index is 97
                break;
    
    return total;

def solve_second_puzzle(file_name):
    lines = parse_file(file_name);

    total = 0;
    for i in range(0, int(len(lines)), 3):
        rucksack_group = lines[i:i+3];
        rucksack_group = list(map(lambda x: x.replace('\n', ''), rucksack_group));
        
        intersection = list(set(rucksack_group[0]) & set(rucksack_group[1]) & set(rucksack_group[2]));
        if len(intersection) != 1:
            raise Exception('Not working yet 👎'); 
        char = intersection[0];
        if isupper(char):
            total += ord(char) - 64 + 26; # ASCII 'A' index is 65
        else:
            total += ord(char) - 96; # ASCII 'a' index is 97
    
    return total;

def parse_file(file_name): 
    file = open(f'day3/input/{file_name}', 'r');
    
    return file.readlines();
