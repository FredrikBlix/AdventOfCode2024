import re

def remove_index(row, index):
    return row[:index] + row[index + 1:]

def problem_dampner(row):
    result = []
    for i in range(len(row)):
        result.append(remove_index(row, i))
    return result

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

def max_difference(row):
    max_diff = 3
    for i in range(len(row) - 1):
        if abs(row[i] - row[i + 1]) > max_diff:
            return False
    return True

def safe(row):
    if not max_difference(row):
        return False
    elif not increasing(row) and not decreasing(row):
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

def part_two(input_data):
    data = parse_input(input_data)
    sum_safe = 0
    for row in data:
        if safe(row):
            sum_safe += 1
        else:
            for row in problem_dampner(row):
                if safe(row):
                    sum_safe += 1
                    break
    return sum_safe
    