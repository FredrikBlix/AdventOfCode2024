import unittest
import os

from partOne import part_one, parse_input

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_one.txt'), 'r') as file:
            self.input_sample_one = file.read()

    def test_part_one(self):
        result = part_one(self.input_sample_one)
        self.assertEqual(result, 11)
    
    def test_parse_input(self):
        result = parse_input(self.input_sample_one)
        self.assertEqual(result, ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]))

if __name__ == '__main__':
    unittest.main()