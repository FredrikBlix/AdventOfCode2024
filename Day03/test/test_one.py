import unittest
import os

from partOne import part_one, parse_input, mul

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_one.txt'), 'r') as file:
            self.input_sample_one = file.read()
  
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

if __name__ == '__main__':
    unittest.main()