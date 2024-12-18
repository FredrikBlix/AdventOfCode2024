import unittest
import os

from partTwo import part_two, parse_input, count_elements_in_list, similarity_score

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_two = file.read()

    def test_part_two(self):
        result = part_two(self.input_sample_two)
        self.assertEqual(result, 31)
    
    def test_parse_input(self):
        result = parse_input(self.input_sample_two)
        self.assertEqual(result, ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]))
        
    def test_count_elements_in_list(self):
        result = count_elements_in_list(1, [1,2,3,4,5])
        self.assertEqual(result, 1)
    
    def test_similarity_score(self):
        result = similarity_score([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()