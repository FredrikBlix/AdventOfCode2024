import unittest
import os

from partTwo import part_two, parse_input, find_number_matches, similarity_score

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_one = file.read()

    def test_part_two(self):
        result = part_two(self.input_sample_one.strip())
        self.assertEqual(result, 31)
    
    def test_parse_input(self):
        result = parse_input(self.input_sample_one.strip())
        self.assertEqual(result, ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]))
        
    def test_find_number_matches(self):
        result = find_number_matches(1, [1,2,3,4,5])
        self.assertEqual(result, 1)
    
    def test_similarity_score(self):
        result = similarity_score([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()