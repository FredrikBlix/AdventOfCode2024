from partOne import part_one
from partTwo import part_two

input_data = None

with open('input.txt', 'r') as file:
    input_data = file.read()

def main():
    result_one = part_one(input_data)
    result_two = part_two(input_data)

    print(f"Result from part one: {result_one}")
    print(f"Result from part two: {result_two}")

if __name__ == "__main__":
    main()