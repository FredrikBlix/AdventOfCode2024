import re

def mul(row):
    sum = 0
    disabled = False
    for operation in row:
        if operation == "do()":
            disabled = False
        elif operation == "don't()":
            disabled = True
        else:
            if disabled:
                continue
            numbers = re.findall(r"\d+", operation)
            sum += int(numbers[0]) * int(numbers[1])
    return sum

def parse_input(input_data):
    return re.findall(r"mul\(\d+\,\d+\)|do\(\)|don\'t\(\)", input_data)

def write_output(output_data, index):
    # Write the output data to a file
    with open(f'row{index}.txt', 'w') as file:
        file.write(str(output_data))
    
def part_two(input_data):
    data = parse_input(input_data)
    return mul(data)    