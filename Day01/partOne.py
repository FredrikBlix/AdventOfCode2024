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

def part_one(input_data, verbose = False):
    left_list, right_list = parse_input(input_data, verbose)
    total_sum = 0;
    for i in range(len(left_list)):
        total_sum +=  abs(left_list[i] - right_list[i])
    return total_sum
