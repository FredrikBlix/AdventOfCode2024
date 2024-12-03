import unittest
import os

from partTwo import part_two, parse_input, mul

class TestMainFunctions(unittest.TestCase):
    
    def read_file(self, filename):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, filename), 'r') as file:
            data = file.read()
        return data
    
    def setUp(self):
        self.input_sample_one = self.read_file('input_sample_one.txt')
        self.input_sample_two = self.read_file('input_sample_two.txt')
        self.input_txt = self.read_file('..\input.txt')
  
    def test_parse_input(self):
        result = parse_input(self.input_sample_one)
        self.assertEqual(result, ['mul(2,4)',
                                   'mul(5,5)',
                                   'mul(11,8)',
                                   'mul(8,5)'])
        result = parse_input(self.input_sample_two)
        self.assertEqual(result, ['mul(2,4)',
                                   "don't()",
                                   'mul(5,5)',
                                   'mul(11,8)',
                                   'do()',
                                   'mul(8,5)'])

    def test_mul(self):
        result = mul(['mul(2,4)',
                      'mul(5,5)',
                      'mul(11,8)',
                      'mul(8,5)'])
        self.assertEqual(result, 161)
    
    def test_mul_2(self):
        result = mul(['mul(2,4)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'do()',
                      'mul(8,5)'])
        self.assertEqual(result, 48)

    def test_mul_3(self):
        result = mul(["don't()",
                      'mul(5,5)'])
        self.assertEqual(result, 0)
        
    def test_mul_4(self):
        result = mul(["do()",
                      'mul(5,5)'])
        self.assertEqual(result, 25)

    def test_mul_5(self):
        result = mul(['do()'])
        self.assertEqual(result, 0)
        
    def test_mul_6(self):
        result = mul(["don't()"])
        self.assertEqual(result, 0)
        
    def test_part_two(self):
        result = part_two(self.input_sample_one)
        self.assertEqual(result, 161)
        result = part_two(self.input_sample_two)
        self.assertEqual(result, 48)
        result = part_two(self.input_txt)
        self.assertEqual(result, 59097164)
        
if __name__ == '__main__':
    unittest.main()