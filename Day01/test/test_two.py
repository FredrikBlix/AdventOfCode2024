import unittest
import os

from partOne import part_one, parse_input, distance_between_points, distance_between_lists

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_one = file.read()

    def test_part_one(self):
        result = part_one(self.input_sample_one.strip())
        self.assertEqual(result, 11)
    
    def test_parse_input(self):
        result = parse_input(self.input_sample_one.strip())
        self.assertEqual(result, ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]))
        
    def test_destance_between_points(self):
        result = distance_between_points(1, 2)
        self.assertEqual(result, 1)
    
    def test_destance_between_lists(self):
        result = distance_between_lists([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()