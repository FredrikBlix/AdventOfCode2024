import re

def mul(row):
    sum = 0
    disabled = False
    for operation in row:
        if "do()" in operation:
            disabled = False
            continue
        elif "don't()" in operation:
            disabled = True
            continue
        
        if disabled:
            continue
                    
        numbers = re.findall(r"\d+", operation)
        sum += int(numbers[0]) * int(numbers[1])
    return sum

def parse_input(input_data):
    list = []
    input_data = input_data.splitlines()
    for row in input_data:
        operations = re.findall(r"mul\(\d+\,\d+\)|do\(\)|don\'t\(\)", row)
        list.append(operations)
    return list

def part_two(input_data):
    data = parse_input(input_data)
    sum = 0
    for row in data:
        sum += mul(row)
    return sum
    