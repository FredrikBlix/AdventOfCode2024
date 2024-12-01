import re

def parse_input(input_data, verbose = False):
    left_list = []
    right_list = []
    row_index = 0
    input_data = input_data.splitlines()

    for row in input_data:
        row_index += 1
        numbers = re.findall(r'\d+', row)

        if verbose:
            print('row [', row_index, '] = ', row, numbers)

        if numbers and len(numbers) == 2:
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
            
    left_list.sort()
    right_list.sort()

    return left_list, right_list

def distance_between_points(x, y):
    return abs(x - y)

def distance_between_lists(left_list, right_list):
    total_sum = 0
    for i in range(len(left_list)):
        total_sum +=  distance_between_points(left_list[i], right_list[i])
    return total_sum

def part_one(input_data, verbose = False):
    left_list, right_list = parse_input(input_data, verbose)
    return distance_between_lists(left_list, right_list)