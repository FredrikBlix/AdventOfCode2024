import re

def parse_input(input_data, verbose = False):
    left_list = []
    right_list = []
    row_index = 0
    input_data = input_data.splitlines()

    for row in input_data:
        row_index += 1
        numbers = re.findall(r'\d+', row)

        if numbers and len(numbers) == 2:
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
            
    left_list.sort()
    right_list.sort()
            
    return left_list, right_list

def find_number_matches(x, list):
    return list.count(x)

def similarity_score(left_list, right_list):
    score = 0
    for i in range(len(left_list)):
        score += left_list[i] * find_number_matches(left_list[i], right_list)
    return score

def part_two(input_data, verbose = False):
    left_list, right_list = parse_input(input_data, verbose)
    return similarity_score(left_list, right_list)