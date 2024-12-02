import re

# Success code is hex FF
SUCCESS = 0xFF

def problem_dampner(row, index):
    row.pop(index) # remove the problem
    if not max_difference(row) == SUCCESS:
        return False
    elif not increasing(row) == SUCCESS and not decreasing(row) == SUCCESS:
        return False
    return True

def increasing(row):
    for i in range(len(row) - 1):
        if row[i] >= row[i + 1]:
            return i + 1
    return SUCCESS

def decreasing(row):
    for i in range(len(row) - 1):
        if row[i] <= row[i + 1]:
            return i + 1
    return SUCCESS

def max_difference(row):
    max_diff = 3
    for i in range(len(row) - 1):
        if abs(row[i] - row[i + 1]) > max_diff:
            return i + 1
    return SUCCESS

def safe(row):
    problem_index_differece = max_difference(row)
    problem_index_increasing = increasing(row)
    problem_index_decreasing = decreasing(row)
    
    if problem_index_differece != SUCCESS:
        return problem_dampner(row, problem_index_differece)
    elif problem_index_increasing != SUCCESS and problem_index_decreasing != SUCCESS:
        return problem_dampner(row, max(problem_index_increasing, problem_index_decreasing))
    return True

def parse_input(input_data):
    list = []
    input_data = input_data.splitlines()
    for row in input_data:
        numbers = re.findall(r'\d+', row)
        numbers = [int(i) for i in numbers]
        list.append(numbers)
    return list

def part_two(input_data):
    data = parse_input(input_data)
    sum_safe = 0
    for row in data:
        if safe(row):
            sum_safe += 1
    return sum_safe
    