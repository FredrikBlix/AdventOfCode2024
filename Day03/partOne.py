import re

def mul(row):
    sum = 0
    for operation in row:
        numbers = re.findall(r"\d+", operation)
        sum += int(numbers[0]) * int(numbers[1])
    return sum

def parse_input(input_data):
    return re.findall(r"mul\(\d+\,\d+\)", input_data)

def part_one(input_data):
    data = parse_input(input_data)
    return mul(data)
    