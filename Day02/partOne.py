import re

def increasing(row):
    for i in range(len(row) - 1):
        if row[i] >= row[i + 1]:
            return False
    return True

def decreasing(row):
    for i in range(len(row) - 1):
        if row[i] <= row[i + 1]:
            return False
    return True

def max_difference(row, max_diff):
    for i in range(len(row) - 1):
        if abs(row[i] - row[i + 1]) > max_diff:
            return False
    return True

def is_it_safe(row):
    
    if not max_difference(row, 3):
        return False
    if not increasing(row) and not decreasing(row):
        return False
    
    return True

def parse_input(input_data):
    list = []
    input_data = input_data.splitlines()
    for row in input_data:
        numbers = re.findall(r'\d+', row)
        numbers = [int(i) for i in numbers]
        list.append(numbers)
    return list

def part_one(input_data):
    data = parse_input(input_data)
    sum_safe = 0
    for row in data:
        if is_it_safe(row):
            sum_safe += 1
    return sum_safe
    