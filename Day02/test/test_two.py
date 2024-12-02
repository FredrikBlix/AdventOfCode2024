import unittest
import os

from partTwo import part_two, parse_input, increasing, decreasing, max_difference, safe

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_one = file.read()
  
    def test_parse_input(self):
        result = parse_input(self.input_sample_one)
        self.assertEqual(result, [[7, 6, 4, 2, 1],
                                  [1, 2, 7, 8, 9],
                                  [9, 7, 6, 2, 1],
                                  [1, 3, 2, 4, 5],
                                  [8, 6, 4, 4, 1],
                                  [1, 3, 6, 7, 9]])
    
    def test_increasing(self):
        result = increasing([1, 2, 3, 4, 5])
        self.assertEqual(result, True)
    
    def test_decreasing(self):
        result = decreasing([5, 4, 3, 2, 1])
        self.assertEqual(result, True)
        
    def test_max_difference(self):
        result = max_difference([1, 2, 3, 4, 5])
        self.assertEqual(result, True)
    
    def test_safe(self):
        result = safe([7, 6, 4, 2, 1])
        self.assertEqual(result, True)
        result = safe([1, 2, 7, 8, 9])
        self.assertEqual(result, False)
        result = safe([9, 7, 6, 2, 1])
        self.assertEqual(result, False)
        result = safe([1, 3, 2, 4, 5])
        self.assertEqual(result, True)
        result = safe([8, 6, 4, 4, 1])
        self.assertEqual(result, True)
        result = safe([1, 3, 6, 7, 9])
        self.assertEqual(result, True)

    def test_part_one(self):
        result = part_two(self.input_sample_one)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()