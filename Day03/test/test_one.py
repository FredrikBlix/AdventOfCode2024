import unittest
import os

from partOne import part_one, parse_input, mul

class TestMainFunctions(unittest.TestCase):

    def read_file(self, filename):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, filename), 'r') as file:
            data = file.read()
        return data

    def setUp(self):
        self.input_sample_one = self.read_file('input_sample_one.txt')
        self.input_txt = self.read_file('..\input.txt')
  
    def test_parse_input(self):
        result = parse_input(self.input_sample_one)
        self.assertEqual(result, [['mul(2,4)',
                                   'mul(5,5)',
                                   'mul(11,8)',
                                   'mul(8,5)']])
        
    def test_mul(self):
        result = mul(['mul(2,4)',
                      'mul(5,5)',
                      'mul(11,8)',
                      'mul(8,5)'])
        self.assertEqual(result, 161)

    def test_part_one(self):
        result = part_one(self.input_sample_one)
        self.assertEqual(result, 161)
        result = part_one(self.input_txt)
        self.assertEqual(result, 183669043)
        
if __name__ == '__main__':
    unittest.main()